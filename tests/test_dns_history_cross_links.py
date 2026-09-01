import unittest
from pathlib import Path


REPOSITORY_ROOT = Path(__file__).resolve().parents[1]
EXPECTED_CROSS_LINKS = (
    (
        Path("docs/software/bind-dns-implementation-history.md"),
        "hosts-txt-to-dns.md",
        "../lineage/hosts-txt-to-dns.md",
    ),
    (
        Path("docs/software/bind-dns-implementation-history.md"),
        "dns-mail-routing-md-mf-mx.md",
        "../lineage/dns-mail-routing-md-mf-mx.md",
    ),
    (
        Path("docs/software/delivermail-sendmail-routing-engine.md"),
        "hosts-txt-to-dns.md",
        "../lineage/hosts-txt-to-dns.md",
    ),
    (
        Path("docs/software/delivermail-sendmail-routing-engine.md"),
        "dns-mail-routing-md-mf-mx.md",
        "../lineage/dns-mail-routing-md-mf-mx.md",
    ),
)


class DNSHistoryCrossLinkTests(unittest.TestCase):
    def test_expected_cross_links_resolve_inside_repository(self) -> None:
        repository_root = REPOSITORY_ROOT.resolve()

        for source_name, label, target_name in EXPECTED_CROSS_LINKS:
            with self.subTest(source=source_name, target=target_name):
                source = (repository_root / source_name).resolve()
                self.assertTrue(
                    source.is_relative_to(repository_root),
                    f"source file escapes repository: {source_name}",
                )
                self.assertTrue(source.is_file(), f"missing source file: {source_name}")
                expected_markup = f"[`{label}`]({target_name})"
                self.assertTrue(
                    expected_markup in source.read_text(encoding="utf-8"),
                    f"{source_name}: missing {expected_markup}",
                )

                target = (source.parent / target_name).resolve()
                self.assertTrue(
                    target.is_relative_to(repository_root),
                    f"cross-link escapes repository: {target_name}",
                )
                self.assertTrue(target.is_file(), f"missing cross-link: {target_name}")


if __name__ == "__main__":
    unittest.main()
