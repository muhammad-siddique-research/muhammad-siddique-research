# Genuine U.S. Data Starter | CDC PLACES 2025 County Data

**Status: source-authenticated ingestion script; real-data download has NOT been executed in this GitHub environment.**

This is a reproducible **data-provenance and schema audit**, not a completed analysis. It retrieves the published CDC PLACES county table directly from the CDC Socrata export endpoint and records a checksum, source URL, retrieval time, row count, county/measure counts, missingness and basic duplicate/range checks.

- Official landing page: https://data.cdc.gov/500-Cities-Places/PLACES-Local-Data-for-Better-Health-County-Data-20/swc5-untb
- Official release notes: https://www.cdc.gov/places/current-release-notes/
- Original source URL used by the script: https://data.cdc.gov/api/views/swc5-untb/rows.csv?accessType=DOWNLOAD
- Data: **model-based county estimates**, not person-level observations. The 2025 release draws largely on earlier BRFSS waves; read metadata carefully.

## Execute on a computer with web access

From this GitHub profile repository's root:

```bash
python us-studies/cdc_places_pilot/download_audit.py
python -m unittest discover -s us-studies/cdc_places_pilot -p 'test_*.py' -v
```

The script writes `us-studies/cdc_places_pilot/data/source.csv` and `manifest.json`, which are ignored by Git. The manifest is local until its provenance and disclosure checks pass. No input data are synthesized or replaced with dummy observations.

## Verification gates

- HTTPS fetch from the named official CDC URL only; abort on network/HTTP failures.
- SHA-256 of exact downloaded bytes, retrieval timestamp and observed record count.
- Normalize source headers and require county FIPS, measure code, state abbreviation and prevalence value fields.
- Count distinct measure codes, counties, missing estimates and negative/out-of-range values.
- Reject duplicate geographic-measure-type keys when that metadata is present. Fail loudly on schema drift.
- **Unit:** county × health indicator × prevalence definition, not individual cases.

**Limitation:** The code has an offline unit-test fixture, which is explicitly synthetic and only tests parsing. A successful synthetic test is NOT proof that a live CDC data download has executed. After a real run, inspect source license, suppression rules, measure denominators and comparability with CMS before modeling.

## Next analysis

Study protocol: [U.S. Healthcare Access, Need & Geographic Variation](../03_health_access.md).
