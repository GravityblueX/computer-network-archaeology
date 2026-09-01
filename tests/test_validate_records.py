from pathlib import Path
import tempfile
import unittest

from scripts.validate_records import (
    LoadedRecord,
    iter_references,
    load_json_object,
    validate_references,
    validate_repository,
)


REPOSITORY_ROOT = Path(__file__).resolve().parents[1]


class StrictJSONLoadingTests(unittest.TestCase):
    def test_rejects_duplicate_keys_at_any_depth(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_directory:
            root = Path(temporary_directory)
            path = root / "record.json"
            path.write_text(
                '{"metadata":{"claim":"first","claim":"second"}}',
                encoding="utf-8",
            )
            errors: list[str] = []

            document = load_json_object(path, root, errors)

        self.assertIsNone(document)
        self.assertEqual(
            ["record.json: invalid JSON: duplicate object key 'claim'"],
            errors,
        )

    def test_rejects_non_finite_numbers(self) -> None:
        for value in ("NaN", "Infinity", "-Infinity"):
            with self.subTest(value=value), tempfile.TemporaryDirectory() as temporary:
                root = Path(temporary)
                path = root / "record.json"
                path.write_text(f'{{"metadata":{{"value":{value}}}}}', encoding="utf-8")
                errors: list[str] = []

                document = load_json_object(path, root, errors)

                self.assertIsNone(document)
                self.assertEqual(
                    [f"record.json: invalid JSON: non-finite number {value!r}"],
                    errors,
                )


class RecordDiscoveryTests(unittest.TestCase):
    def test_rejects_noncanonical_record_locations(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_directory:
            root = Path(temporary_directory)
            normal = root / "records/artifacts/ART-9996.json"
            nested = root / "records/artifacts/nested/ART-9997.json"
            unknown = root / "records/unknown/ART-9998.json"
            uppercase = root / "records/sources/SRC-9999.JSON"
            for path in (normal, nested, unknown, uppercase):
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_text("{}", encoding="utf-8")

            report = validate_repository(root)

        self.assertEqual(
            {"artifact": 1, "source": 0, "lineage": 0},
            report.record_counts,
        )
        self.assertIn(
            "records/artifacts/nested/ART-9997.json: JSON records must be "
            "directly inside a registered record directory",
            report.errors,
        )
        self.assertIn(
            "records/unknown/ART-9998.json: unregistered record directory 'unknown'",
            report.errors,
        )
        self.assertIn(
            "records/sources/SRC-9999.JSON: JSON record extension must be .json",
            report.errors,
        )

    def test_rejects_record_symlink_outside_repository(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_directory:
            base = Path(temporary_directory)
            root = base / "repository"
            record_directory = root / "records/artifacts"
            record_directory.mkdir(parents=True)
            external_record = base / "external.json"
            external_record.write_text("{}", encoding="utf-8")
            symlink = record_directory / "ART-9999.json"
            external_directory = base / "external-sources"
            external_directory.mkdir()
            directory_symlink = root / "records/sources"
            try:
                symlink.symlink_to(external_record)
                directory_symlink.symlink_to(
                    external_directory, target_is_directory=True
                )
            except (NotImplementedError, OSError) as error:
                self.skipTest(f"cannot create symlinks on this platform: {error}")

            report = validate_repository(root)

        self.assertEqual(0, report.record_counts["artifact"])
        self.assertEqual(
            1,
            report.errors.count(
                "records/artifacts/ART-9999.json: resolves outside repository root"
            ),
        )
        self.assertEqual(
            1,
            report.errors.count(
                "records/sources: resolves outside repository root"
            ),
        )


class ReferenceExtractionTests(unittest.TestCase):
    def test_extracts_references_from_each_record_shape(self) -> None:
        artifact = {
            "parent_family": "ART-0001",
            "chronology": {
                "announced": {"source_ids": ["SRC-0001", "SRC-0002"]}
            },
            "sources": [{"source_id": "SRC-0003"}],
            "related_artifacts": [{"id": "ART-0002", "relation": "revision-of"}],
        }
        source = {
            "artifact_ids": ["ART-0003"],
            "claims_extracted": [{"artifact_ids": ["ART-0004"]}],
        }
        lineage = {
            "from": {"artifact_id": "ART-0005"},
            "to": {"artifact_id": "ART-0006"},
            "sources": [{"source_ref": "SRC-0004; SRC-0005"}],
        }

        actual = {
            (reference.target_group, reference.target_id)
            for group, document in (
                ("artifact", artifact),
                ("source", source),
                ("lineage", lineage),
            )
            for reference in iter_references(group, document)
        }

        self.assertEqual(
            {
                ("artifact", f"ART-{number:04d}") for number in range(1, 7)
            }
            | {("source", f"SRC-{number:04d}") for number in range(1, 6)},
            actual,
        )

    def test_unknown_reference_reports_its_json_path(self) -> None:
        path = REPOSITORY_ROOT / "records/artifacts/ART-9999-example.json"
        records = [
            LoadedRecord(
                "artifact",
                path,
                {"id": "ART-9999", "sources": [{"source_id": "SRC-9999"}]},
            )
        ]
        errors = validate_references(
            records,
            {"artifact": {"ART-9999"}, "source": set(), "lineage": set()},
            REPOSITORY_ROOT,
        )

        self.assertEqual(
            [
                "records/artifacts/ART-9999-example.json:$.sources[0].source_id: "
                "unknown source ID SRC-9999"
            ],
            errors,
        )


class RepositoryValidationTests(unittest.TestCase):
    def test_repository_evidence_graph_is_valid(self) -> None:
        report = validate_repository(REPOSITORY_ROOT)
        self.assertEqual([], report.errors, "\n".join(report.errors))
        self.assertGreater(report.total_records, 400)


if __name__ == "__main__":
    unittest.main()
