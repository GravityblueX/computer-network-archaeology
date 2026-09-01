from pathlib import Path
import tempfile
import unittest

from scripts.validate_records import GROUP_BY_NAME, load_ledger_ids


GROUP_CASES = (
    ("artifact", "ART-9999"),
    ("source", "SRC-9999"),
    ("lineage", "LIN-9999"),
)


class LedgerCSVContractTests(unittest.TestCase):
    def load_ledger(
        self,
        group_name: str,
        content: str,
    ) -> tuple[set[str], list[str]]:
        with tempfile.TemporaryDirectory() as temporary_directory:
            root = Path(temporary_directory)
            group = GROUP_BY_NAME[group_name]
            ledger_path = root / group.ledger
            ledger_path.parent.mkdir(parents=True)
            ledger_path.write_text(content, encoding="utf-8")
            errors: list[str] = []

            ledger_ids = load_ledger_ids(
                root,
                group,
                errors,
            )

        return ledger_ids, errors

    def test_accepts_a_quoted_field_containing_commas(self) -> None:
        for group_name, record_id in GROUP_CASES:
            with self.subTest(group=group_name):
                group = GROUP_BY_NAME[group_name]
                ledger_ids, errors = self.load_ledger(
                    group_name,
                    f"{group.ledger_id_column},title,archive_or_mirror\n"
                    f'{record_id},Example,"https://example.test/a,b,c"\n',
                )

                self.assertEqual({record_id}, ledger_ids)
                self.assertEqual([], errors)

    def test_accepts_a_utf8_bom_before_the_id_header(self) -> None:
        for group_name, record_id in GROUP_CASES:
            with self.subTest(group=group_name):
                group = GROUP_BY_NAME[group_name]
                ledger_ids, errors = self.load_ledger(
                    group_name,
                    f"\ufeff{group.ledger_id_column},title\n"
                    f"{record_id},Example\n",
                )

                self.assertEqual({record_id}, ledger_ids)
                self.assertEqual([], errors)

    def test_rejects_duplicate_header_names(self) -> None:
        for group_name, record_id in GROUP_CASES:
            with self.subTest(group=group_name):
                group = GROUP_BY_NAME[group_name]
                ledger_ids, errors = self.load_ledger(
                    group_name,
                    f"{group.ledger_id_column},title,title\n"
                    f"{record_id},First title,Second title\n",
                )

                self.assertEqual(set(), ledger_ids)
                self.assertEqual(
                    [f"{group.ledger}: duplicate ledger column(s): 'title'"],
                    errors,
                )

    def test_rejects_blank_header_names(self) -> None:
        for group_name, record_id in GROUP_CASES:
            group = GROUP_BY_NAME[group_name]
            for blank_header in ("", "   "):
                with self.subTest(group=group_name, blank_header=blank_header):
                    ledger_ids, errors = self.load_ledger(
                        group_name,
                        f"{group.ledger_id_column},{blank_header}\n"
                        f"{record_id},discarded value\n",
                    )

                    self.assertEqual(set(), ledger_ids)
                    self.assertEqual(
                        [
                            f"{group.ledger}: blank ledger column name(s) "
                            "at position(s): 2"
                        ],
                        errors,
                    )

    def test_rejects_a_row_with_overflow_fields(self) -> None:
        for group_name, record_id in GROUP_CASES:
            with self.subTest(group=group_name):
                group = GROUP_BY_NAME[group_name]
                ledger_ids, errors = self.load_ledger(
                    group_name,
                    f"{group.ledger_id_column},title\n"
                    f"{record_id},Example,unexpected\n",
                )

                self.assertEqual(set(), ledger_ids)
                self.assertEqual(
                    [
                        f"{group.ledger}:2: malformed CSV row has 3 fields; "
                        "expected 2"
                    ],
                    errors,
                )

    def test_reports_the_physical_line_after_blank_lines(self) -> None:
        for group_name, record_id in GROUP_CASES:
            with self.subTest(group=group_name):
                group = GROUP_BY_NAME[group_name]
                ledger_ids, errors = self.load_ledger(
                    group_name,
                    f"{group.ledger_id_column},title\n"
                    "\n"
                    f"{record_id},Example,unexpected\n",
                )

                self.assertEqual(set(), ledger_ids)
                self.assertEqual(
                    [
                        f"{group.ledger}:3: malformed CSV row has 3 fields; "
                        "expected 2"
                    ],
                    errors,
                )

    def test_reports_the_physical_line_after_a_multiline_field(self) -> None:
        for group_name, record_id in GROUP_CASES:
            with self.subTest(group=group_name):
                group = GROUP_BY_NAME[group_name]
                second_id = record_id[:-4] + "9998"
                ledger_ids, errors = self.load_ledger(
                    group_name,
                    f"{group.ledger_id_column},title\n"
                    f'{record_id},"First line\nSecond line"\n'
                    f"{second_id},Example,unexpected\n",
                )

                self.assertEqual({record_id}, ledger_ids)
                self.assertEqual(
                    [
                        f"{group.ledger}:4: malformed CSV row has 3 fields; "
                        "expected 2"
                    ],
                    errors,
                )

    def test_rejects_an_unterminated_quoted_field(self) -> None:
        for group_name, record_id in GROUP_CASES:
            with self.subTest(group=group_name):
                group = GROUP_BY_NAME[group_name]
                second_id = record_id[:-4] + "9998"
                ledger_ids, errors = self.load_ledger(
                    group_name,
                    f"{group.ledger_id_column},title\n"
                    f'{record_id},"unterminated\n'
                    f"{second_id},Next\n",
                )

                self.assertEqual(set(), ledger_ids)
                self.assertEqual(1, len(errors))
                self.assertTrue(
                    errors[0].startswith(
                        f"{group.ledger}:3: invalid CSV: "
                    ),
                    errors[0],
                )

    def test_rejects_a_row_with_missing_fields(self) -> None:
        for group_name, record_id in GROUP_CASES:
            with self.subTest(group=group_name):
                group = GROUP_BY_NAME[group_name]
                ledger_ids, errors = self.load_ledger(
                    group_name,
                    f"{group.ledger_id_column},title,notes\n"
                    f"{record_id},Example\n",
                )

                self.assertEqual(set(), ledger_ids)
                self.assertEqual(
                    [
                        f"{group.ledger}:2: malformed CSV row has 2 fields; "
                        "expected 3"
                    ],
                    errors,
                )


if __name__ == "__main__":
    unittest.main()
