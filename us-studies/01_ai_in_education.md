# U.S. Study 01 | AI in Education: Adoption, Governance and Equity

**Stage:** PROTOCOL — no new data extracted or empirical result reported.  
**Domain:** Educational Data Science · AI in Education · Policy Measurement

## Research question

How do U.S. public schools differ in reported **AI-related policies, teacher training, instructional use and administrators’ perceptions**, and how sensitive are these patterns to school characteristics and survey design?

The question is about **measured readiness and governance**, not whether adopting AI causes higher student achievement.

## Verified data source

- **Producer:** National Center for Education Statistics (NCES), School Pulse Panel (SPP).
- **Public results:** https://nces.ed.gov/surveys/spp/results.asp
- **Program overview and survey materials:** https://nces.ed.gov/surveys/spp/
- **Relevant release:** December 2024 SPP AI/technology module, with published estimates and standard errors. Data are school-level survey summaries, not matched student test scores.
- **Initial item domains:** written student AI policy; administrators' views of student/teacher AI use; teachers using AI for planning; teacher AI training; AI-use instruction for students. Download exact question wording and table notes before using any variable.

## Testable hypotheses (unverified)

- **H1:** Reported formal AI policy adoption is heterogeneous by school characteristics; direction unspecified.
- **H2:** Teacher AI professional development and instructional-use reports are associated at a descriptive subgroup level; joint school microdata would be required to estimate school-level associations.
- **H3:** Apparent subgroup contrasts attenuate after respecting published survey standard errors and multiple testing.

## Design and analysis

1. Retrieve official dated aggregate results, standard errors, category definitions, questionnaire wording and disclosure notes.
2. Define one table per questionnaire item × subgroup × survey month; never join separately published marginal tables as if they describe the same school.
3. Calculate weighted published contrasts with uncertainty only as design permits; correct for multiplicity and report survey response/nonresponse limitations.
4. Develop reproducible visualizations of uncertainty intervals and policy/training differences; distinguish unavailable statistics from zero.
5. Benchmark any forecasting task against a transparent constant or stratified-rate baseline; do not train a learner-level risk model on school aggregates.

**Threats:** school self-report, selection/nonresponse, ecological inference, policy and use measured together, temporal overlap, multiple testing and access limitations.

**What would overturn a substantive pattern?** Differences that reverse under harmonized reference periods or lie inside survey-consistent uncertainty bounds.

**Causal extension (separate design):** Only with independently documented exogenous policy variation, longitudinal outcomes at the appropriate unit, validated parallel-trends/overlap assumptions, and pre-intervention covariates. None is present in this protocol.

**Initial output:** exact-source data manifest + descriptive and uncertainty-aware AI governance brief. No sample sizes or findings invented.
