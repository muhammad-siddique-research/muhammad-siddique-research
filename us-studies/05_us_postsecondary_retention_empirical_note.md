# Manuscript 01 | U.S. Postsecondary Retention and Institutional Composition (2021–2024)

**Status:** **EXECUTED AGGREGATE ANALYSIS / WORKING MANUSCRIPT — NOT JOURNAL-READY**  
**Researcher:** Muhammad Siddique, PhD  
**Prepared:** 26 November 2026  
**Domain:** Institutional Research · Educational Data Science · Computational Economics

## Research question

How much of the aggregate full-time versus part-time early-retention gap in U.S. postsecondary education is attributable *algebraically* to within-institution-level rate differences versus the different institutional-level composition of entering students?

This is **not a study of AI adoption or a causal effect of part-time attendance**. A journal-level extension requires substantially richer data and a differentiated literature contribution.

## Genuine official data and scope

Three original published NCES IPEDS national retention tables were used:

- **Fall 2021 entrants → fall 2022:** [NCES Table 8, final](https://nces.ed.gov/ipeds/search/viewtable?tableId=36097)
- **Fall 2022 entrants → fall 2023:** [NCES Table 2, provisional](https://nces.ed.gov/ipeds/search/viewtable?tableId=36438)
- **Fall 2023 entrants → fall 2024:** [NCES Table 2, provisional](https://nces.ed.gov/ipeds/search/viewtable?tableId=36543)

The executed **54-cell** dataset comprises three report years × three broad institution levels × three control types × two initial enrollment-intensity categories. The 54 disjoint sector/intensity/year counts sum to **7,559,111 annual cohort memberships**, **not** unique individuals tracked longitudinally. Reconstructed control subgroups exactly sum to the **18 source-reported institution-level × year × intensity totals**.

**Crucial provenance distinction:** These are authentic NCES-published **national aggregate counts transcribed and checked** for the analysis. The original institution-level IPEDS CSV files were **not downloaded and analyzed** in this first draft. Therefore no institution-specific effects, held-out ML results, individual-level outcomes or identified causal relationships are claimed.

## Results: executed arithmetic from authentic published counts

| Fall outcome year | Full-time retention | Part-time retention | National difference |
|---|---:|---:|---:|
| 2022 | 76.62% | 45.82% | 30.80 percentage points |
| 2023 | 77.52% | 46.50% | 31.02 percentage points |
| 2024 | 77.86% | 46.95% | 30.92 percentage points |

### Heterogeneity of observed rate gaps

| Fall outcome year | 4-year institutions | 2-year institutions | Less-than-2-year institutions |
|---|---:|---:|---:|
| 2022 | 31.95 pp | 19.82 pp | 4.48 pp |
| 2023 | 32.17 pp | 20.68 pp | 6.02 pp |
| 2024 | 32.69 pp | 20.22 pp | 7.99 pp |

### Symmetric level-composition decomposition (exact identity)

| Year | Within-level rate component | Institution-level composition component | Total observed gap |
|---|---:|---:|---:|
| 2022 | 24.78 pp | 6.02 pp | 30.80 pp |
| 2023 | 25.33 pp | 5.68 pp | 31.02 pp |
| 2024 | 25.40 pp | 5.51 pp | 30.92 pp |

The terms are **descriptive accounting identities, not causal explanations or estimates of the benefits of switching enrollment intensity**. The lower-than-four-year definition can include completed certificates while four-year retention is generally continuing enrollment; pooled figures do not measure identical educational outcomes across all levels. Provisional vintages and changing Title IV support are additional limitations.

## Scientific and publication status

- **Completed:** real federal published counts inspected, cell-level transcription, exact 18-margin checks, national rate calculations, within-level heterogeneity, direct standardization, symmetrical rate/composition decomposition, two generated figures, and working manuscript draft.
- **Pending:** independent full IPEDS institution-level source downloads, versioned longitudinal harmonization, complete literature novelty audit, formal inferential design, out-of-time ML benchmarks (if justified), causal policy identification (if feasible), external replication, journal targeting and peer review.
- **Novelty alert:** [Vamosiu & Conroy (2026)](https://doi.org/10.1002/berj.70094) already study institutional full-/part-time retention differences with a much richer community-college panel; this initial national-aggregate analysis cannot be presented as a first discovery.
- **Policy application:** inform comparability of institutional benchmarks and selection of subsequent evaluations, not prescribe a proven treatment.

A complete editable manuscript, the official-table reconstruction script, all 54 source-identified cell counts, computed CSV tables, and two figures were generated as a separate **conversation research package** on 26 November 2026. They have **not yet been committed into this repository**; this note records results and provenance transparently without pretending that the public repository contains files it does not.

**Next stage:** obtain authentic IPEDS EF20xxD, HD20xx, student aid, and institutional attributes for sufficient years; verify UNITID, outcome cohort definition, sample support and source vintage; build a genuine institution-year panel; develop distinct hypotheses and defensible associations/forecast evaluation; only then decide journal submission feasibility.

[Research program](../../US_RESEARCH_PROGRAM.md) · [Publication and national-impact standards](../../research-standards/JOURNAL_PUBLICATION_AND_NATIONAL_IMPACT.md)
