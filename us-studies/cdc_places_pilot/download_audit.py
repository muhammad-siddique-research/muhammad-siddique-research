#!/usr/bin/env python3
"""Fetch authentic CDC PLACES public county data and audit its provenance.

No numerical research finding is produced here. Failure to fetch official data
is an error: this program never falls back to simulated observations.
"""
from __future__ import annotations

import csv
import hashlib
import io
import json
import re
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

SOURCE_URL = "https://data.cdc.gov/api/views/swc5-untb/rows.csv?accessType=DOWNLOAD"
SOURCE_PAGE = (
    "https://data.cdc.gov/500-Cities-Places/"
    "PLACES-Local-Data-for-Better-Health-County-Data-20/swc5-untb"
)
DATA_DIR = Path(__file__).resolve().parent / "data"


def canonical(field: str) -> str:
    return re.sub(r"[^a-z0-9]", "", field.casefold())


def audit_csv(content: bytes) -> dict:
    """Validate the authentic source's tabular structure, not its scientific claims."""
    try:
        reader = csv.DictReader(io.StringIO(content.decode("utf-8-sig")))
    except UnicodeError as exc:
        raise ValueError("Source is not readable as UTF-8 CSV") from exc
    names = reader.fieldnames or []
    aliases = {canonical(name): name for name in names}
    required = {"locationid", "stateabbr", "measureid", "datavalue"}
    missing = sorted(required - aliases.keys())
    if missing:
        raise ValueError("CDC source schema missing required columns: " + ", ".join(missing))
    keycols = ["locationid", "measureid"]
    if "datavaluetypeid" in aliases:
        keycols.append("datavaluetypeid")
    elif "datavaluetype" in aliases:
        keycols.append("datavaluetype")
    elif "datavaluetypename" in aliases:
        keycols.append("datavaluetypename")
    else:
        raise ValueError("CDC source is missing the prevalence-type identifier")
    seen = set()
    counties = set()
    measures = set()
    count = 0
    blank = 0
    for row in reader:
        count += 1
        county = (row[aliases["locationid"]] or "").strip()
        state = (row[aliases["stateabbr"]] or "").strip()
        measure = (row[aliases["measureid"]] or "").strip()
        if not re.fullmatch(r"\d{5}", county) or not state or not measure:
            raise ValueError(f"Invalid county/state/measure identifier at CSV record {count}")
        key = tuple((row[aliases[col]] or "").strip() for col in keycols)
        if key in seen:
            raise ValueError(f"Duplicated county/measure/prevalence key at record {count}: {key!r}")
        seen.add(key)
        counties.add(county)
        measures.add(measure)
        raw_value = (row[aliases["datavalue"]] or "").strip()
        if not raw_value or raw_value.upper() in {"NA", "N/A", "NULL"}:
            blank += 1
            continue
        try:
            value = float(raw_value)
        except ValueError as exc:
            raise ValueError(f"Non-numeric estimate at record {count}") from exc
        if not 0 <= value <= 100:
            raise ValueError(f"Percentage outside [0,100] at CSV record {count}")
    if count == 0:
        raise ValueError("Official CDC download produced no rows")
    return {
        "observed_rows": count,
        "unique_county_ids": len(counties),
        "unique_measure_codes": len(measures),
        "missing_data_value_rows": blank,
        "raw_headers": names,
        "unique_key": keycols,
        "estimate_check": "Data_Value parsed as percentage in [0,100] where reported",
    }


def main() -> None:
    request = urllib.request.Request(
        SOURCE_URL, headers={"User-Agent": "USResearchAudit/1.0 (public source verification)"}
    )
    with urllib.request.urlopen(request, timeout=120) as response:
        content = response.read()
    audit = audit_csv(content)
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    (DATA_DIR / "source.csv").write_bytes(content)
    manifest = {
        "producer": "U.S. Centers for Disease Control and Prevention",
        "dataset": "CDC PLACES county data, 2025 release (verify API vintage)",
        "source_page": SOURCE_PAGE,
        "exact_download_url": SOURCE_URL,
        "retrieved_utc": datetime.now(timezone.utc).isoformat(),
        "sha256_original_csv": hashlib.sha256(content).hexdigest(),
        "downloaded_bytes": len(content),
        "source_evidence_class": "A: official public model-based estimates",
        "underlying_period_note": "2025 release is based largely on BRFSS 2023/2022, not 2025 patient observations",
        "scientific_status": "DATA_ACQUIRED_AND_SCHEMA_AUDITED; NO EMPIRICAL MODELS",
        "audit": audit,
    }
    (DATA_DIR / "manifest.json").write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"status": "AUDITED", "manifest": str(DATA_DIR / "manifest.json"), **audit}, indent=2))


if __name__ == "__main__":
    main()
