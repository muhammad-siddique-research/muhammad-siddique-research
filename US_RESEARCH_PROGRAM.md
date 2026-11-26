# U.S. Evidence-First Research Program (2026–2027)

**Research lead:** Muhammad Siddique, PhD  
**Portfolio lens:** Computational Economics × Educational Data Science × Responsible AI/ML  
**Initial status (25 November 2026):** Research designs and source verification; **not results, published manuscripts, or registered studies**.

## Decision

From this point forward, prioritize **original U.S.-focused empirical studies addressing emerging economic, educational, and healthcare problems**, using verifiable authentic datasets. Existing international and historical projects remain labeled and preserved; they are not retroactively reclassified as U.S. 2026 evidence. Synthetic data may be used for software testing or methods demonstrations only, never as a substitute for observational or experimental results.

## Ranked portfolio

| Priority | Question | Source / units | Research contribution sought | Feasibility / caveat |
|---|---|---|---|---|
| **1 — AI in Education** | Do AI governance, teacher training and reported use vary across U.S. public schools? | NCES School Pulse Panel, published school-survey estimates and standard errors | Transparent school-policy and readiness measurement; distinguish policy adoption from student learning impacts | **High** for descriptive inference, **low** for causal student effects from aggregate published tables |
| **2 — Institutional Research** | Which U.S. institutional conditions forecast retention/completion, and how stable are rankings across institution types? | NCES IPEDS and U.S. Department of Education College Scorecard, institution-level cohorts | Leakage-aware longitudinal benchmarks and institutional effectiveness audit | **High**, but cohort definitions and privacy suppressions matter; not an AI adoption study |
| **3 — Economics of AI** | How does U.S. firm-reported AI use vary by industry and business function, and what labor-market shifts coincide with diffusion? | Census BTOS published indicators + separately defined BLS public labor statistics | Measurement and timing audit, calibrated descriptive comparisons; exploratory forecasting | **Moderate**: aggregation and survey revisions limit causal attribution |
| **4 — Healthcare Access** | Where do Medicare utilization/spending patterns diverge from modeled community health needs? | CMS Original Medicare Geographic Variation PUF + CDC PLACES 2025 county models | Geographic mismatch and uncertainty diagnostics, not patient-level cost-effectiveness | **Moderate**: ecological analysis, selective Medicare population and modeled PLACES prevalence |

**Interdisciplinary contribution:** use a consistent evaluation architecture across domains while respecting very different units of analysis, data-generation mechanisms, and identification constraints.

## What makes a study eligible for a main empirical claim?

1. **An official or otherwise traceable source**: owner, landing page, release date, file or API URL, access date, license, data dictionary, checksum or exact query.
2. **Unit-of-analysis documentation**: school, institution-year, industry/time period, or county-year. Never infer individual effects from aggregate data.
3. **An independent data audit**: observed row counts, uniqueness keys, geographic/temporal support, suppression and missingness, variable provenance, and revision history.
4. **Precommitted comparisons**: transparent baseline, purposeful Econometric specification, genuinely separated train/validation/test periods or groups, uncertainty and robust sensitivity checks.
5. **Proper statistical interpretation**: model-specific predictions versus associations versus causal effects, data limitations, confounding and potential selection mechanisms.
6. **Reproducible output**: code, environment, tests, provenance manifest, regenerable tables and figures, and transparent inability to release any restricted records.
7. **Publication-readiness gate**: substantive literature review, replication pass, all figure/table reconciliation, and a limitations section. Do not call a prototype a manuscript or a manuscript a peer-reviewed publication.

See [Evidence Policy](research-standards/EVIDENCE_POLICY.md).

## First experiments (no unverified findings reported)

**Sprint A — School AI governance (NCES).** Download NCES School Pulse Panel published AI-related results and standard errors; version all data and question wording; compare subgroup estimates with uncertainty under the published survey design. **Falsification**: observed descriptive differences disappear after design-consistent uncertainty or harmonizing questionnaire windows. **Not a causal study of AI learning impacts.**

**Sprint B — Institution-level effectiveness (IPEDS/Scorecard).** Retrieve named collection-year CSV files and dictionaries, audit UNITID/OPEID keys, cohort outcome definitions and changes over time, establish a naive baseline and pooled/regularized institutional models with forward-year holdout. **Falsification**: predictive gain vanishes out of time, or depends on unavailable post-outcome variables. **Not individual student prediction.**

**Sprint C — County healthcare evidence (CDC/CMS).** Execute the [CDC PLACES reproducible ingestion and schema audit](us-studies/cdc_places_pilot/README.md) using genuine CDC county data; inspect CMS geography, coverage, and date alignment before merging. **Falsification**: a county association fails after support alignment or realistic uncertainty. **Not beneficiary-level causal inference.**

**Sprint D — Economics of AI (Census).** Audit the Census BTOS AI/SI series for wording, geography, sector, reference periods, and redefinitions. Build transparent descriptive tables before considering a matched BLS panel. **Falsification**: apparent time trends reflect changing definitions or composition. **Not a claim that AI changed employment.**

## Primary-source entry points

- U.S. NCES School Pulse Panel: https://nces.ed.gov/surveys/spp/results.asp
- NCES IPEDS data: https://nces.ed.gov/ipeds/datacenter/DataFiles.aspx?gotoReportId=7
- U.S. College Scorecard data: https://collegescorecard.ed.gov/data/
- U.S. Census BTOS data: https://www.census.gov/hfp/btos/data
- CMS Medicare geographic variation: https://data.cms.gov/tools/geographic-variation-in-standardized-medicare-spending-state
- CDC PLACES 2025 county release: https://data.cdc.gov/500-Cities-Places/PLACES-Local-Data-for-Better-Health-County-Data-20/swc5-untb

**Source qualification:** Link availability and public descriptions have been checked; an executed source-data audit is still needed before any numerical finding is published. Webpage last-modified dates are not equivalent to underlying survey/reference dates.

## Study sequence

**Data acquisition and provenance → research design and feasibility audit → baseline results → robustness and uncertainty → literature/novelty verification → manuscript and replicable artifacts.** An original research result is reported only after its computations are actually executed and validated.
