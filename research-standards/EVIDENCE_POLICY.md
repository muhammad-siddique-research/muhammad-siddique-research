# Data Provenance and Scientific Evidence Policy

**Applies to all new U.S. empirical projects in this portfolio.** Date adopted: 25 November 2026. This is a workflow standard, not an assertion that existing studies have already satisfied every requirement.

**Additional mandatory standard:** [Journal-Quality Research & U.S. National Impact Framework](JOURNAL_PUBLICATION_AND_NATIONAL_IMPACT.md). This adds primary-literature novelty verification, theoretical contribution, publication-ready robustness, policy decision relevance, and verified evidence of dissemination. A paper does not pass because it has a high word count or many models.

## Allowed evidence classes

| Class | Examples | What can be claimed |
|---|---|---|
| **A — Authentic public empirical data** | NCES IPEDS, College Scorecard, Census BTOS published outputs, CMS aggregate public-use records, CDC PLACES | Clearly scoped descriptive estimates or observational models after verified acquisition and successful analysis |
| **B — Authorized restricted/original empirical data** | Private institutional survey or restricted research data accessed with permission | Only validated results permitted by consent, contracts, IRB and disclosure controls; never publish restricted raw records |
| **C — Synthetic / simulated / demonstration data** | Generated classroom tests, Monte Carlo experiments | Methods and software behavior **only**, unless the explicitly synthetic experiment itself is the object of study |
| **D — Proposed/archived/unreplicated claims** | Planned protocol, older aggregate extract without independent rerun | Hypotheses and historical reported figures *with status and limits*; never relabel as newly validated results |

## Required study manifest

For every data-bearing analysis publish: dataset title and federal producer; official URL; retrieval timestamp and release vintage; the reference year(s) of underlying observations; lawful access and licenses; SHA-256 of input files; variables and transformations; observation unit; inclusion/exclusion rules; sampling/survey weights; missing/suppressed codes; join keys; quality checks; versioned environment; and regeneration commands. For mutable APIs, archive a timestamped query and source metadata as available.

## Required scientific gates

1. **Source gate:** official extract obtained and checksum recorded. A clickable dataset link alone is insufficient.
2. **Schema gate:** dictionary-to-column verification; confirm units, variable definitions, and vintage.
3. **Support gate:** target population, geographic and temporal coverage, denominator, suppression and missingness.
4. **Design gate:** clearly label estimand, prediction target or descriptive question; justify assumptions for any causal identification.
5. **Evaluation gate:** meaningful baseline, leakage control, grouped/temporal out-of-sample validation where applicable; survey-consistent standard errors.
6. **Robustness gate:** alternative specifications, uncertainty, dependence/cluster structure, distribution shift, fairness where relevant and null/negative results.
7. **Release gate:** all results executable from authorized inputs or transparently disclosed if unreplicated, limitations written, citations verified.

## Non-negotiable distinctions

- **Real data is not necessarily causal data.** Even genuine source records cannot establish an effect without a defensible design.
- **Observed federal aggregates differ from individual records.** CMS public-use tables are not full claims files, NCES published school estimates are not person-level student outcomes, and PLACES prevalence estimates are statistically modeled rather than directly observed in every county.
- **The latest release is not the latest observation year.** CDC PLACES 2025 includes underlying BRFSS 2022/2023 data. Verify each cohort and source vintage.
- **A scripted downloader is not evidence of a completed data analysis.** No row count, coefficient, sample or figure is claimed until execution is documented.
- **Never fabricate novelty, citations, outcomes, confidence intervals or sample sizes.** Verify literature against primary publications before calling a result new.
- **No sensitive or protected data on GitHub.** Use public aggregates, licensed public-use extracts, or fully authorized de-identified datasets with verified disclosure permissions.

## Project statuses

Use one of: `PROTOCOL`, `DATA_ACQUIRED`, `AUDITED`, `EXPLORATORY_RESULTS`, `REPLICATED_RESULTS`, `PREPRINT`, `PEER_REVIEWED`. Promote a status only with a linked evidence artifact. No model score or study population should be inferred from a status name.
