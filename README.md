# Muhammad Siddique
### Interdisciplinary Researcher | Economist | Education Data Science & Explainable AI

**Econometrics · Predictive Machine Learning · Computational Social Science · Higher Education Policy**

I develop **theory-grounded, reproducible research** at the intersection of economics, education, and artificial intelligence. My focus is to move responsibly from **statistical association** to **validated prediction**, and ultimately to **evidence-informed decisions** that improve institutional practice and student experiences.

My research toolkit brings together **applied econometrics, HC3-robust inference, model diagnostics, regularized regression, XGBoost, LightGBM, Random Forest, Tree SHAP, and research-to-policy translation**.

## Featured Scholarship

### [The Science of Student Thriving: Econometrics and Explainable AI Analysis](https://github.com/muhammad-siddique-research/higher-ed-flourishing-prediction-ml-xai)

*Revised scholarly manuscript (working paper; not represented as published or peer reviewed)*

A single-institution undergraduate survey examined the association of **sense of community, institutional integrity, and spirituality** with the Thriving Quotient, integrating replicated econometric results and exploratory explainable machine learning.

| Study and methodological evidence | Finding |
|---|---|
| Original undergraduate survey | **N = 156** |
| Complete-case primary regression and ML analysis | **n = 152** |
| Replicated ordinary least squares model | **R² = .436**; adjusted **R² = .424** |
| Community association (HC3 robust) | **B = .405**, 95% CI **[.267, .543]** |
| Internal XGBoost prediction | Mean five-times-repeated 5-fold **RMSE = .379** |
| Random Forest comparison | **RMSE = .380** — effectively comparable |
| Explainable AI | Community received the largest mean absolute held-out Tree SHAP attribution |

The key contribution is **methodological triangulation**: classical regression provides conditional associations and uncertainty; held-out ML tests predictive utility; Tree SHAP reveals the fitted model's feature reliance. **None of these analyses establishes causality or generalization to new institutions.**

<details>
<summary><b>Research integrity and reproducibility</b></summary>

- The numerical results above derive from **the original privately analyzed SPSS survey**, not the repository's separate synthetic demonstrations.
- Seven model configurations were evaluated on **25 overlapping matched validation folds (5 folds × 5 repeats)**. Differences between XGBoost and Random Forest are too small to claim clear algorithmic superiority.
- Tree SHAP was calculated on withheld cases during the first 5-fold repetition. Its feature attributions do **not** imply intervention effects.
- **Participant-level student data and respondent-level SHAP graphics remain restricted**. Only aggregate results and methodological documentation are public.
- Study authorization, scale psychometrics, coauthor approval, and journal-specific disclosures require confirmation before submission.

</details>

[**Empirical results and privacy-safe figures →**](https://github.com/muhammad-siddique-research/higher-ed-flourishing-prediction-ml-xai/blob/main/docs/REAL_DATA_VALIDATION.md) ·
[**Project repository and methods →**](https://github.com/muhammad-siddique-research/higher-ed-flourishing-prediction-ml-xai) ·
[**Higher education policy agenda →**](https://github.com/muhammad-siddique-research/higher-ed-flourishing-prediction-ml-xai/blob/main/docs/EDUCATION_POLICY_BRIEF.md)

## Research Agenda

- **Student thriving and institutional effectiveness:** belonging, campus climate, trust, spirituality, psychosocial measurement, and equitable student success
- **Econometric identification and robustness:** linear modeling, HC3 robust errors, influence diagnostics, specification checks, uncertainty and sensitivity analysis
- **Explainable predictive modeling:** regularization, tree ensembles, repeated cross-validation, predictive stability, and Tree SHAP interpretation
- **Educational policy and evaluation:** student-centered mentoring, faculty–student engagement, inclusive support design, and prospective intervention evaluation
- **Economic and financial analytics:** quantitative modeling, economic decision support, and computational risk analysis

## Additional Research Repositories

- **[E-Commerce Purchase Prediction](https://github.com/muhammad-siddique-research/ecommerce-purchase-prediction-ml)** — classification and interpretable consumer-behavior analytics
- **[Financial Risk and Explainable AI](https://github.com/muhammad-siddique-research/financial-risk-ai)** — computational financial-risk modeling

## Technical Methods

**Python · statsmodels · pandas · NumPy · SciPy · scikit-learn · XGBoost · LightGBM · SHAP · Streamlit · GitHub Actions · Stata · IBM SPSS Statistics**

My research emphasizes **transparent estimation, defensible uncertainty, reproducible workflows, and educationally meaningful interpretation**—not prediction without governance or policy claims without an evaluation design.

> *Rigorous computation matters most when its assumptions are visible, its limitations are understood, and its insights can be tested in educational practice.*
