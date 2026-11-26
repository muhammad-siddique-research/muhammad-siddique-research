# U.S. Study 03 | Healthcare Access, Need and Geographic Variation

**Stage:** PROTOCOL — no CMS/CDC merge or health-effect estimate has been executed.  
**Domain:** Computational Health Economics · Spatial and Ecological Quantitative Research

## Research question

Where do county-level **Original Medicare utilization and standardized spending** patterns appear discordant with modeled community health needs, and how much of that comparison is sensitive to population, geography and measurement uncertainty?

## Authentic official source foundation

- **CMS Original Medicare Geographic Variation** (public-use aggregate records / data dashboard): https://data.cms.gov/tools/geographic-variation-in-standardized-medicare-spending-state
- **CMS Geographic Variation PUF methods and scope**: https://data.cms.gov/summary-statistics-on-use-and-payments/medicare-geographic-comparisons
- **CDC PLACES 2025 county release**: https://data.cdc.gov/500-Cities-Places/PLACES-Local-Data-for-Better-Health-County-Data-20/swc5-untb
- **CDC methodology and data caveats**: https://www.cdc.gov/places/about/

**Critical vintage warning:** PLACES '2025 release' is not 2025 clinical observations; measures largely use 2023 BRFSS and some 2022 BRFSS. CMS's reporting year may differ. Release dates and measurement years must be included separately in every table.

## Research design

1. Execute [the CDC PLACES source ingestion and audit](cdc_places_pilot/README.md). Its code downloads **genuine public CDC records**; no real download or result is claimed until an output manifest exists.
2. Download corresponding CMS geographic files with source dictionary, selected denominator (Original Medicare), standardized spending/utilization measures, suppression flags and annual vintage.
3. Validate 5-digit county FIPS, reporting-year alignment, Medicare population denominators, available years, and county boundary changes; document unmatched counties.
4. Compare directly **within the observed supported populations**. PLACES is a model-derived general-adult prevalence series, not a patient-level Medicare diagnosis rate.
5. Start with descriptive maps and correlation/sensitivity analysis; report ecological uncertainty and regional dependence. Only then consider robust multivariable analysis or out-of-region prediction, with explicit baselines and held-out geographies.

## Pre-specified propositions

- **H1:** County rankings of need versus service provision depend materially on the selected need and utilization definitions.
- **H2:** Apparent associations change when accounting for region, urbanicity and Medicare enrollment composition.
- **H3:** Any county prediction has weaker transportability to held-out regions than a naive random-split evaluation suggests.

**Potential rejection:** Results disappear with fixed county support, appropriate denominator, release vintage, clustering or relevant confounders.

**Causal and ethical limit:** No individual patient linkage; no claim that a given expenditure causes a county health outcome, no claim of diagnostic individual risk, and no use of restricted medical data.

**First deliverable:** a verified CDC data-provenance manifest, followed by a two-source compatibility audit before any inferential estimates.
