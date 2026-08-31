from pathlib import Path
import unittest

from scripts.validate_records import (
    LoadedRecord,
    iter_references,
    validate_references,
    validate_repository,
)


REPOSITORY_ROOT = Path(__file__).resolve().parents[1]


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
