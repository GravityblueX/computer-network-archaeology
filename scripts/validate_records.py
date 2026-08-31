#!/usr/bin/env python3
"""Validate the repository's structured evidence graph.

The JSON Schemas protect each record in isolation.  This script adds the
repository-level invariants that JSON Schema cannot express: stable IDs,
filename/ID agreement, ledger identities, and references between records.
"""

from __future__ import annotations

import argparse
import csv
import json
import re
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Iterator, Mapping, Sequence

from jsonschema import Draft202012Validator, FormatChecker
from jsonschema.exceptions import SchemaError


@dataclass(frozen=True)
class RecordGroup:
    name: str
    directory: str
    schema: str
    id_prefix: str
    ledger: str
    ledger_id_column: str

    @property
    def id_pattern(self) -> re.Pattern[str]:
        return re.compile(rf"{self.id_prefix}-[0-9]{{4,}}")


GROUPS: tuple[RecordGroup, ...] = (
    RecordGroup(
        "artifact",
        "records/artifacts",
        "schema/artifact-record.schema.json",
        "ART",
        "data/artifact-ledger.csv",
        "artifact_id",
    ),
    RecordGroup(
        "source",
        "records/sources",
        "schema/source-record.schema.json",
        "SRC",
        "data/source-ledger.csv",
        "source_id",
    ),
    RecordGroup(
        "lineage",
        "records/lineages",
        "schema/lineage-edge.schema.json",
        "LIN",
        "data/lineage-ledger.csv",
        "lineage_id",
    ),
)

GROUP_BY_NAME = {group.name: group for group in GROUPS}
SOURCE_ID_TOKEN = re.compile(r"\bSRC-[0-9]{4,}\b")


@dataclass(frozen=True)
class LoadedRecord:
    group: str
    path: Path
    document: dict[str, object]


@dataclass(frozen=True)
class Reference:
    target_group: str
    target_id: str
    json_path: str


@dataclass
class ValidationReport:
    errors: list[str]
    record_counts: dict[str, int]
    ledger_counts: dict[str, int]

    @property
    def total_records(self) -> int:
        return sum(self.record_counts.values())


def display_path(path: Path, root: Path) -> str:
    try:
        return path.relative_to(root).as_posix()
    except ValueError:
        return path.as_posix()


def json_path(parts: Sequence[object]) -> str:
    rendered = "$"
    for part in parts:
        if isinstance(part, int):
            rendered += f"[{part}]"
        else:
            rendered += f".{part}"
    return rendered


def schema_error_sort_key(error: object) -> tuple[tuple[tuple[int, object], ...], str]:
    """Return a key that remains comparable when paths mix keys and indexes."""

    absolute_path = getattr(error, "absolute_path")
    message = getattr(error, "message")
    path_key = tuple(
        (0, part) if isinstance(part, int) else (1, str(part))
        for part in absolute_path
    )
    return path_key, message


def load_json_object(path: Path, root: Path, errors: list[str]) -> dict[str, object] | None:
    label = display_path(path, root)
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, UnicodeError) as error:
        errors.append(f"{label}: cannot read UTF-8 JSON: {error}")
        return None
    except json.JSONDecodeError as error:
        errors.append(
            f"{label}:{error.lineno}:{error.colno}: invalid JSON: {error.msg}"
        )
        return None

    if not isinstance(value, dict):
        errors.append(f"{label}: expected a JSON object at the document root")
        return None
    return value


def load_schema(
    path: Path, root: Path, errors: list[str]
) -> dict[str, object] | None:
    schema = load_json_object(path, root, errors)
    if schema is None:
        return None
    try:
        Draft202012Validator.check_schema(schema)
    except SchemaError as error:
        errors.append(
            f"{display_path(path, root)}:{json_path(list(error.absolute_path))}: "
            f"invalid JSON Schema: {error.message}"
        )
        return None
    return schema


def load_ledger_ids(
    root: Path, group: RecordGroup, errors: list[str]
) -> set[str]:
    path = root / group.ledger
    label = display_path(path, root)
    ids: set[str] = set()
    try:
        handle = path.open(encoding="utf-8-sig", newline="")
    except OSError as error:
        errors.append(f"{label}: cannot read ledger: {error}")
        return ids

    with handle:
        reader = csv.DictReader(handle)
        if reader.fieldnames is None or group.ledger_id_column not in reader.fieldnames:
            errors.append(
                f"{label}: missing required column {group.ledger_id_column!r}"
            )
            return ids
        for line_number, row in enumerate(reader, start=2):
            record_id = (row.get(group.ledger_id_column) or "").strip()
            if not group.id_pattern.fullmatch(record_id):
                errors.append(
                    f"{label}:{line_number}: invalid {group.ledger_id_column} "
                    f"{record_id!r}; expected {group.id_prefix}- followed by at least four digits"
                )
                continue
            if record_id in ids:
                errors.append(f"{label}:{line_number}: duplicate ledger ID {record_id}")
                continue
            ids.add(record_id)
    return ids


def strings(value: object) -> Iterator[tuple[int, str]]:
    if not isinstance(value, list):
        return
    for index, item in enumerate(value):
        if isinstance(item, str):
            yield index, item


def iter_references(group: str, document: Mapping[str, object]) -> Iterator[Reference]:
    """Yield typed ID references from one record, with their JSON paths."""

    if group == "artifact":
        parent_family = document.get("parent_family")
        if isinstance(parent_family, str) and GROUP_BY_NAME["artifact"].id_pattern.fullmatch(
            parent_family
        ):
            yield Reference("artifact", parent_family, "$.parent_family")

        chronology = document.get("chronology")
        if isinstance(chronology, dict):
            for milestone, claim in chronology.items():
                if not isinstance(claim, dict):
                    continue
                for index, source_id in strings(claim.get("source_ids")):
                    yield Reference(
                        "source",
                        source_id,
                        f"$.chronology.{milestone}.source_ids[{index}]",
                    )

        sources = document.get("sources")
        if isinstance(sources, list):
            for index, claim in enumerate(sources):
                if isinstance(claim, dict) and isinstance(claim.get("source_id"), str):
                    yield Reference(
                        "source", claim["source_id"], f"$.sources[{index}].source_id"
                    )

        related = document.get("related_artifacts")
        if isinstance(related, list):
            for index, relation in enumerate(related):
                if isinstance(relation, dict) and isinstance(relation.get("id"), str):
                    yield Reference(
                        "artifact", relation["id"], f"$.related_artifacts[{index}].id"
                    )

    elif group == "source":
        for index, artifact_id in strings(document.get("artifact_ids")):
            yield Reference("artifact", artifact_id, f"$.artifact_ids[{index}]")

        claims = document.get("claims_extracted")
        if isinstance(claims, list):
            for claim_index, claim in enumerate(claims):
                if not isinstance(claim, dict):
                    continue
                for artifact_index, artifact_id in strings(claim.get("artifact_ids")):
                    yield Reference(
                        "artifact",
                        artifact_id,
                        f"$.claims_extracted[{claim_index}].artifact_ids[{artifact_index}]",
                    )

    elif group == "lineage":
        for endpoint_name in ("from", "to"):
            endpoint = document.get(endpoint_name)
            if isinstance(endpoint, dict) and isinstance(endpoint.get("artifact_id"), str):
                yield Reference(
                    "artifact", endpoint["artifact_id"], f"$.{endpoint_name}.artifact_id"
                )

        sources = document.get("sources")
        if isinstance(sources, list):
            for index, claim in enumerate(sources):
                if not isinstance(claim, dict) or not isinstance(
                    claim.get("source_ref"), str
                ):
                    continue
                for source_id in SOURCE_ID_TOKEN.findall(claim["source_ref"]):
                    yield Reference(
                        "source", source_id, f"$.sources[{index}].source_ref"
                    )


def validate_references(
    records: Sequence[LoadedRecord], known_ids: Mapping[str, set[str]], root: Path
) -> list[str]:
    errors: list[str] = []
    for record in records:
        for reference in iter_references(record.group, record.document):
            if reference.target_id not in known_ids[reference.target_group]:
                errors.append(
                    f"{display_path(record.path, root)}:{reference.json_path}: "
                    f"unknown {reference.target_group} ID {reference.target_id}"
                )
    return errors


def validate_repository(root: Path) -> ValidationReport:
    root = root.resolve()
    errors: list[str] = []
    record_counts = {group.name: 0 for group in GROUPS}
    ledger_counts = {group.name: 0 for group in GROUPS}
    records: list[LoadedRecord] = []
    structured_ids: dict[str, set[str]] = {group.name: set() for group in GROUPS}
    ledger_ids: dict[str, set[str]] = {group.name: set() for group in GROUPS}
    seen_structured_ids: dict[str, Path] = {}

    for group in GROUPS:
        schema_path = root / group.schema
        schema = load_schema(schema_path, root, errors)
        validator = (
            Draft202012Validator(schema, format_checker=FormatChecker())
            if schema is not None
            else None
        )

        record_directory = root / group.directory
        if not record_directory.is_dir():
            errors.append(
                f"{display_path(record_directory, root)}: record directory does not exist"
            )
            paths: list[Path] = []
        else:
            paths = sorted(record_directory.glob("*.json"))

        for path in paths:
            document = load_json_object(path, root, errors)
            if document is None:
                continue
            record_counts[group.name] += 1
            records.append(LoadedRecord(group.name, path, document))

            if validator is not None:
                schema_errors = sorted(
                    validator.iter_errors(document),
                    key=schema_error_sort_key,
                )
                for error in schema_errors:
                    errors.append(
                        f"{display_path(path, root)}:{json_path(list(error.absolute_path))}: "
                        f"{error.message}"
                    )

            record_id = document.get("id")
            if not isinstance(record_id, str):
                continue
            structured_ids[group.name].add(record_id)
            previous_path = seen_structured_ids.get(record_id)
            if previous_path is not None:
                errors.append(
                    f"{display_path(path, root)}: duplicate structured ID {record_id}; "
                    f"already used by {display_path(previous_path, root)}"
                )
            else:
                seen_structured_ids[record_id] = path

            if path.stem != record_id and not path.stem.startswith(f"{record_id}-"):
                errors.append(
                    f"{display_path(path, root)}: filename must be {record_id}.json "
                    f"or start with {record_id}-"
                )

        ledger_ids[group.name] = load_ledger_ids(root, group, errors)
        ledger_counts[group.name] = len(ledger_ids[group.name])

    known_ids = {
        group.name: structured_ids[group.name] | ledger_ids[group.name]
        for group in GROUPS
    }
    errors.extend(validate_references(records, known_ids, root))
    errors.sort()
    return ValidationReport(errors, record_counts, ledger_counts)


def parse_args(argv: Sequence[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--root",
        type=Path,
        default=Path(__file__).resolve().parents[1],
        help="repository root (defaults to the parent of this script's directory)",
    )
    return parser.parse_args(argv)


def main(argv: Sequence[str] | None = None) -> int:
    args = parse_args(argv)
    report = validate_repository(args.root)
    if report.errors:
        print(
            f"Validation failed with {len(report.errors)} error(s):",
            file=sys.stderr,
        )
        for error in report.errors:
            print(f"- {error}", file=sys.stderr)
        return 1

    counts = ", ".join(
        f"{group.name}s={report.record_counts[group.name]}"
        for group in GROUPS
    )
    ledger_counts = ", ".join(
        f"{group.name}s={report.ledger_counts[group.name]}"
        for group in GROUPS
    )
    print(
        f"Validated {report.total_records} structured records ({counts}); "
        f"ledger identities: {ledger_counts}."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
