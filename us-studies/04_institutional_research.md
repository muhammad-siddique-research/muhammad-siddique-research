# U.S. Study 04 | Institutional Effectiveness and Student Outcomes

**Stage:** PROTOCOL — no new results calculated.  
**Domain:** Institutional Research · Educational Data Science · Quantitative Evaluation

## Research question

How well can **publicly observed institutional conditions** anticipate subsequent retention, completion or affordability indicators across U.S. colleges, and when do apparently strong models lose accuracy across years or institutional sectors?

## Genuine data sources

- **NCES Integrated Postsecondary Education Data System (IPEDS):** https://nces.ed.gov/ipeds/
- **IPEDS downloadable survey files and metadata:** https://nces.ed.gov/ipeds/datacenter/DataFiles.aspx?gotoReportId=7
- **U.S. Department of Education College Scorecard:** https://collegescorecard.ed.gov/data/
- **College Scorecard institution-level documentation:** https://collegescorecard.ed.gov/files/InstitutionDataDocumentation.pdf

Source files include institution-level aggregates, not individual student histories. Different graduation, outcome, enrollment and retention cohorts can refer to different student populations and time windows; use official cohort maps. Confirm each downloaded year is **provisional or final**.

## Hypotheses to test

- **H1:** A transparent multivariate baseline improves upon a prior-year/institution-sector baseline for held-out-year prediction.
- **H2:** Nonlinear ML yields only limited or unstable improvements over regularized statistical baselines once leakage is prevented.
- **H3:** Error and calibration patterns vary by institutional type, cohort definitions and student-population context.

## Design

1. Acquire and hash official institution-level yearly source files and dictionaries.
2. Construct a pre-specified outcome definition with year-specific cohort map, UNITID/OPEID audit and pre-outcome covariates.
3. Do not mix incompatible institution reporting levels; carefully document mergers, closure, year gaps, missing and privacy-suppressed cells.
4. Create first-year prevalence/lagged-outcome benchmarks, regularized regression and a limited tree model comparison.
5. Use **forward-year holdout** and institution-aware evaluation; report MAE/RMSE/calibration as appropriate, missingness, subgroup error and uncertainty.
6. Assess proxy fairness, coverage and failure modes before discussing institutional decision support.

**What this does not prove:** effects of AI in teaching, causal impacts of spending, or specific effects on individual students. No learner-level intervention is present.

**First deliverable:** harmonized institution-year variable inventory, cohort map, leakage audit, and a reproducible baseline report.
