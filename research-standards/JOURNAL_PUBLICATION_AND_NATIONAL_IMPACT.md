# Journal-Quality Research & U.S. National Impact Framework

**Adopted:** 25 November 2026  
**Purpose:** Guide all new U.S.-focused empirical studies toward publication in reputable peer-reviewed journals and defensible evidence of public-policy relevance.  
**Status:** Research-governance protocol, **not a publication, impact finding, or assurance of journal acceptance or immigration benefit**.

## Research mission

Produce original, independently reproducible research on emerging problems in the U.S. economy, education and healthcare using **authentic, lawful, traceable U.S. datasets**. Connect Computational Economics, Educational Data Science, Advanced Econometrics, Causal Inference research design and Responsible AI/ML to decisions that matter for U.S. institutions, workers, students and communities.

**One strong, substantively novel paper with verified empirical findings takes priority over many partially audited draft papers.**

### Publication and impact are distinct standards

- **Scientific test:** original contribution, credible theory and estimands, authentic data, methods appropriate to the causal/predictive/descriptive question, transparent uncertainty, robustness and reproducible results.
- **Journal test:** clearly defined audience, fit with peer-reviewed outlet, novelty relative to recent primary literature, data/code disclosure consistent with law, editorial ethics and credible handling of review critiques.
- **Public-policy test:** decision-makers and intervention margins identified in advance; policy choices compared under stated evidence limitations; feasible implementation, cost, distributional effects and possible unintended consequences assessed where data permit.
- **National-interest evidence test:** document how a coherent proposed endeavor could address a nationally relevant U.S. challenge, what work has **actually** been done, independent dissemination/uptake, collaborations or citations if they occur, and how the researcher is positioned to continue. **Do not confuse a publication with guaranteed immigration eligibility.**

USCIS policy (as of 2025 NIW update): https://www.uscis.gov/policy-manual/volume-6-part-f-chapter-5  
USCIS NIW policy update: https://www.uscis.gov/sites/default/files/document/policy-manual-updates/20250115-Employment-BasedNationalInterestWaivers.pdf

The NIW petition is assessed under the specific proposed endeavor and applicable adjudicatory standard; seek immigration counsel for legal interpretation. GitHub documentation is research evidence, not legal advice or proof of policy impact.

## Mandatory journal-quality gates

| Gate | Deliverable | Stop/revise trigger |
|---|---|---|
| **G0 — U.S. public relevance** | National-scale U.S. issue, who is affected, policy decision, theoretical mechanism, target journal audience | Merely rebranding a generic model-comparison as a national problem |
| **G1 — Novelty** | Structured primary-literature matrix: at least 15 highly relevant papers where available, including 2024–2026 research; distinguish exact overlap, method, data, estimand and contribution | Recent paper already resolves the same empirical question with better data and design |
| **G2 — Source feasibility** | Download genuine source, data dictionary, observation/reference years, source vintage, authorization and checksums; verify outcome and exposure can be observed at compatible units | A proposed merge invents individual records, unsupported joins or an outcome absent from the data |
| **G3 — Theoretical model** | Mechanism, alternative explanations, precise hypotheses, unit of analysis, potential channels, and estimand | Theory not linked to measured variables |
| **G4 — Credible design** | Predeclared descriptive/forecasting/causal objective; identification assumptions only for causal claims; DAG where useful, confounding and selection threats | Claims of AI effect based only on ecological correlations or contemporaneous associations |
| **G5 — Estimation & comparison** | Transparent baseline, Econometric models, only justified ML, survey weights, standard errors, clustering, time/group split and leakage diagnostics | Weak benchmark, flawed sampling inference or post-outcome predictors |
| **G6 — Robustness & falsification** | Sensitivity to support, measures, model family, temporal windows, sample, multiple testing, placebo/negative controls when identified, heterogeneity, fairness and null results | Finding driven by one fragile specification or unaddressed measurement break |
| **G7 — Policy contribution** | Which decision changes, whose welfare matters, operational constraints, uncertainty, and plausible implementation or evaluation | Policy conclusions exceed identified evidence |
| **G8 — Independent replication** | Clean environment, pipeline execution log, tests, tables/figures rebuilt, documented omissions/restricted data, external reproducibility review where feasible | Numbers copied from notes without source-to-result execution |
| **G9 — Journal submission** | Venue-specific manuscript, current author instructions, ethics statement, contributions, data/code availability, cover letter, reviewer objection audit and references | Manuscript inflated by word count or claims more than data show |
| **G10 — Dissemination and evidence** | DOI/status, accepted paper or truthful preprint status, documented presentations, uptake and citations if verified | Self-asserted influence, simulated usage metrics or presumed acceptance |

**Do not pursue significant p-values as a deliverable.** A well-reproduced null finding or design failure is valid evidence and can redirect the project.

## Current research strategy — feasibility before ambition

| Candidate | Hypothesis/contribution to test | Current source support and novelty risk | Recommended role |
|---|---|---|---|
| **A. U.S. AI in schools** | Whether national school AI governance/readiness contrasts persist under survey-corrected measurement and school-type heterogeneity | NCES School Pulse Panel published aggregates/SE; not linked to learning outcomes, so no AI-learning causal claim. Descriptive adoption is already reported by NCES. **Novelty unverified, potential substantive ceiling.** | **Fast authentic-data feasibility pilot; not automatically flagship journal paper** |
| **B. U.S. institutional effectiveness** | Whether institution-level prediction of subsequent retention/completion generalizes across cohorts and sectors, and what uncertainty-aware rankings imply for student-support allocation | IPEDS + College Scorecard support institution-level longitudinal analyses, subject to cohort/UNITID alignment. Prediction literature is crowded. **Needs distinctive pre-specified problem and robust generalization test.** | **Most feasible data-rich flagship candidate, subject to literature audit** |
| **C. U.S. Economics of AI and labor adjustment** | Measurement-aware comparison of AI diffusion with labor-market outcomes; *only* estimate causal effects if credible exogenous variation is independently demonstrated | Census BTOS + BLS public aggregates do not alone identify employment effects; several strong 2026 studies already examine adoption. **High national relevance, high novelty and design risk.** | **Ambitious second flagship after overlap and data-grain audit** |
| **D. Healthcare access and geographic need** | Whether spending/use-versus-health-need mismatch rankings are robust to denominator, geography, uncertainty and population support | CMS Original Medicare aggregates + CDC PLACES modeled general-population prevalence: incompatible populations require explicit design and uncertainty treatment. **No beneficiary-level inference.** | **Parallel feasibility project; do not use as causal claims study without new design** |

**Trade-off:** Publication prospects depend on the empirical contribution, not on choosing the most fashionable AI topic. Neither prestigious outlets nor NIW outcomes can be promised.

## First methodological experiment to prioritize

**Working question:** *Do institutional-level educational outcome forecasts remain calibrated and decision-useful when transferred to different U.S. college sectors and later cohorts?*

- **Theory:** resource constraint, student composition and institutional context imply potentially unstable associations; model complexity may overfit historical structures.
- **H1:** A longitudinal regularized baseline improves forward-year prediction relative to a sector/lagged-outcome baseline.
- **H2:** Flexible ML's random-split advantage attenuates in forward-year and held-out-sector validation.
- **H3:** Model error and calibration vary materially by institution type and enrollment characteristics.
- **Data:** publicly obtainable NCES IPEDS and U.S. College Scorecard institution-level panels with exact collection vintages; **not student-level causal data**.
- **Methods:** harmonized cohort-year panel; lagged-outcome and Elastic Net baselines; modest Gradient Boosting; grouped/time-split nested model selection; MAE, RMSE, calibration, worst-sector error and uncertainty; sensitivity to institutional changes and missingness.
- **Falsification:** ML gain vanishes under strict forward holdout; rates differ because of cohort definitions; apparent effectiveness is due to post-outcome leakage.
- **Policy decision:** help institutional researchers prioritize **where to audit outcome measurement or support programs**, not infer that an individual institution's intervention is causally effective.
- **First experiment:** acquire two documented source vintages, verify join keys (UNITID/OPEID), cohort definitions, time ordering and unsuppressed outcomes before any model fitting.

**Publication caveat:** This initial study is not claimed novel or sufficient for an A-tier journal until the literature map and empirical design show a meaningful contribution. A separate quasi-experimental design would be needed for causal policy impact.

## Journal selection, not a promise of acceptance

Potential reputable **scope-based targets**, only after the research question and evidence are established:

- **Educational Evaluation and Policy Analysis** (AERA): original, rigorous, multidisciplinary education policy research. https://www.aera.net/Publications/Journals/Educational-Evaluation-and-Policy-Analysis
- **Journal of Educational and Behavioral Statistics** (AERA): educational measurement/statistical methodology when the work is a genuine methods contribution. https://www.aera.net/Publications/Journals
- **Economics of Education Review**: Economics-of-Education framing when economic mechanisms, identification and policy contribution are sufficiently developed. https://www.sciencedirect.com/journal/economics-of-education-review
- **Journal of Health Economics**: for a substantive health-economics identification and welfare question, not a generic ML comparison. https://www.sciencedirect.com/journal/journal-of-health-economics
- **Research Policy**: for an original, empirically credible innovation-diffusion/policy contribution with a strong theoretical mechanism. https://www.sciencedirect.com/journal/research-policy

Check the **current** submission scope, methods expectations, open-access requirements and author instructions immediately before selection. Do not infer ranking, acceptance probability or suitability from a journal title alone.

## Literature overlap alert — U.S. Economics of AI

The following **2026 primary studies** overlap generic AI adoption and firm AI exposure research. They must be compared **before** presenting a new contribution:

1. U.S. Census Bureau. (2026, September). *AI Exposure and Adoption Among U.S. Firms* (CES-WP-26-61). https://www.census.gov/library/working-papers/2026/adrm/CES-WP-26-61.html
2. U.S. Census Bureau. (2026). *The Microstructure of AI Diffusion: Evidence from Firms, Business Functions, and Worker Tasks* (CES-WP-26-25). https://www.census.gov/library/working-papers/2026/adrm/CES-WP-26-25.html
3. Board of Governors of the Federal Reserve System. (2026, April 3). *Monitoring AI Adoption in the U.S. Economy.* https://www.federalreserve.gov/econres/notes/feds-notes/monitoring-ai-adoption-in-the-u-s-economy-20260403.html

**Consequence:** An additional descriptive report of AI-use trends by sector is **not yet a defensible novelty claim**. Either establish a clearly new estimand, population, measurement contribution or research design, or pivot.

## Evidence for scholarly and public impact

For every actual completed study maintain an audit trail of: source and analysis versions; authorship and contributions; DOI/peer-review status; replication materials; legitimate external references; independently documented collaboration; citation records; externally verifiable policy or practice uptake if any; and a concise **U.S. public-value brief** that clearly labels results versus recommendations.

Never frame hypothetical impact or acceptance as already achieved. The research record should be scientifically defensible even without an immigration application.
