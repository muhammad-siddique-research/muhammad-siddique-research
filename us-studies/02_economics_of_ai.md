# U.S. Study 02 | Economics of AI: Business Adoption and Labor-Market Adjustment

**Stage:** PROTOCOL — no empirical estimates produced.  
**Domain:** Computational Economics · Economics of AI · Labor Economics

## Research question

How is reported U.S. business AI adoption distributed across industries and business functions, how do definitions and survey periods affect apparent diffusion, and what employment or wage patterns **co-occur** in comparable published labor statistics?

## Official authentic sources

- **U.S. Census Bureau, Business Trends and Outlook Survey (BTOS):** https://www.census.gov/hfp/btos/data
- **BTOS downloads and metadata:** https://www.census.gov/hfp/btos/data_downloads
- **U.S. BLS Quarterly Census of Employment and Wages:** https://www.bls.gov/cew/downloadable-data-files.htm
- **BLS Current Employment Statistics:** https://www.bls.gov/ces/

Census updated AI supplement questions in late 2025. Verify **AI vs 'SI' wording**, survey dates, sector/population definitions, weighting, mode changes and the level of publicly available geography before assembling a series. Do not presume firm-level microdata are openly available.

## Hypotheses for testing (not findings)

- **H1:** Reported AI use varies across business functions and industry groups after accounting for publication definitions.
- **H2:** Some apparent diffusion changes shrink after survey-question and reference-window harmonization.
- **H3:** An industry/time model incorporating prior reported AI-use indicators outperforms a naive previous-period baseline at **forecasting published AI-use rates**, if comparable panel data exist.

## Method

1. Download dated official aggregate extracts, questionnaire and release notes; store immutable manifest.
2. Build a dimension registry: industry/NAICS mapping, geography, survey week, reference period, AI definition, numerator, denominator, and weighting/SE.
3. First analyze **Census AI adoption alone** at its observed units. Treat BLS labor measures as separate outcomes until geographic/industry/date support is established.
4. Descriptive pooled comparisons; seasonality/series break diagnostics and robust sensitivity around revised survey wording.
5. Only when adequate comparable periods exist: leakage-free out-of-time benchmark against lagged constant and simple statistical baselines.
6. Report weights, SEs, missing/suppressed cells, compositional shifts, and the limits of selected survey respondents.

**Identification boundary:** Concurrent labor-market changes are not attributable to AI from sector-level co-movement; causal analysis would require a separate defensible source of exogenous exposure. Do not estimate a fictional treatment effect.

**First deliverable:** data-vintage crosswalk and descriptive AI-use measurement study, followed by a feasibility decision for labor-market integration.
