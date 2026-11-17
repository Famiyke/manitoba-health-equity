# Project 6: Manitoba Regional Health Equity Analysis

> **PROJECT VALIDATION STATUS:** The Python demonstration workflow has passed GitHub Actions. Generated model parameters and subgroup comparisons are synthetic. No synthetic values should be described as verified official health-system statistics. See [SOURCE_VALIDATION.md](SOURCE_VALIDATION.md) for the evidence boundary.\n\n
> **DATA PROVENANCE:** This portfolio project uses simulated records informed by named Canadian public sources. All generated statistics, rankings, demographic differences, and savings models are illustrative rather than verified official estimates. Recommendations are hypothetical scenarios, not observed effects.

**Domain:** Health Equity / Social Determinants of Health
**Tools:** Python · SQL · Excel
**Public reference source (distinct from simulated analysis data):** Manitoba Health Annual Statistics
**Download:** https://www.gov.mb.ca/health/annstats/
(Free — PDF reports by year, extract tables manually into Excel)

---

## Business Question
Which Regional Health Authorities in Manitoba carry the highest burden of chronic disease, premature mortality, and health service underutilisation, and what social determinants explain the gaps?

---

## How to Get the Real Data
1. Go to: https://www.gov.mb.ca/health/annstats/
2. Download the latest Annual Statistics report (PDF)
3. Open in Adobe or your browser and find tables for:
   - Mortality by RHA and cause
   - Physician visits per capita by RHA
   - Hospital separations by RHA
   - Diabetes and hypertension prevalence by RHA
4. Copy table values manually into `manitoba_rha_data.xlsx`
5. Export as CSV and run `python analysis.py`

## How to Run (demo mode)
```bash
pip install pandas numpy openpyxl
python simulate_manitoba.py   # creates manitoba_rha.csv (~25 rows)
python analysis.py            # full analysis with equity scores and recommendations
```

---

## Analyst Roles

| Hat | What I Did |
|-----|-----------|
| Data Detective | Extracted 9 indicator tables from Manitoba Health PDF reports, standardised RHA names, validated totals against provincial aggregates |
| SQL/Python Programmer | Ranked RHAs on composite health equity score, correlated social determinants with mortality, built year-over-year trend analysis |
| Dashboard Architect | Built Excel workbook with 4 sheets: Summary KPIs, RHA indicator comparison with equity scores, Northern RHA trend analysis, and social determinant correlations |
| Data Storyteller | Produced a plain-language equity brief for a Manitoba Health committee |
| Strategic Consultant | Recommended three place-based investments targeting the Northern, Prairie Mountain, and Interlake-Eastern RHAs |

---

## Illustrative analytical outputs

This project's Python/SQL outputs illustrate data processing, comparisons, modeling and reporting using generated records. The specific rates, rankings, cost figures and trends in the demonstration are **not verified official findings**. See the analysis scripts for the computations and the data limitations section below for interpretation requirements.

## Excel Workbook

**File:** `manitoba_health_equity.xlsx`

| Sheet | Contents |
|-------|---------|
| Summary | KPI cards for Northern RHA, 4 key findings with supporting text |
| RHA Indicators | All 5 RHAs × 9 indicators, composite equity score, bar chart |
| Northern RHA Trends | Year-over-year trend 2018–2022 with COVID annotation, gap vs provincial average |
| Social Determinants | Correlation table — low income, no doctor, and smoking vs mortality rate |

---

## Interpretation and real-world next steps

Use the simulated findings to demonstrate analytical methods, not to rank actual jurisdictions or recommend clinical or policy interventions. A real decision requires matched official data, documented definitions, relevant uncertainty, and clinical or operational stakeholder review. Financial scenarios must include assumptions, costs and sensitivity analysis.

## Files

| File | Purpose |
|------|---------|
| `simulate_manitoba.py` | Builds representative RHA-level data using synthetic assumptions not verified against provincial tables |
| `analysis.py` | RHA profile, Northern gap analysis, composite equity score, social determinant correlations, trend analysis |
| `sql_queries.sql` | 7 SQL queries covering RHA snapshot, burden index, COVID impact, and diabetes growth |
| `manitoba_health_equity.xlsx` | Excel workbook with 4 sheets — Summary, RHA Indicators, Northern Trends, Social Determinants |
| `equity_brief.md` | Plain-language brief for a Manitoba Health planning committee |

---

## Data Provenance and Limitations

The RHA dataset is simulated. The 41.5% no-doctor rate, composite equity score and mortality association do not constitute official Manitoba Health estimates. A correlation among only five regions cannot establish causation. Document indicator sources, index weights, denominators and uncertainty before applying this analysis to policy.

Manitoba Health Annual Statistics are published as PDF reports, not downloadable CSVs. This project uses simulated data anchored to published RHA-level indicators from the Manitoba Health Annual Statistics 2022–23 report. The simulation script documents all source figures inline. The analytical methodology reflects the approach used in provincial health planning roles.

---

## Reproducibility and execution status

**Environment:** Python 3 with `pandas` and `numpy` installed. If working with the Excel files, install `openpyxl` as needed. Run the simulation script before the analysis commands shown above.

**Important:** The scripts are designed for the generated datasets and expected column names. Downloading a public government table does **not** guarantee that it will run with these scripts unchanged; a schema-mapping and validation step is required for authentic external data. The generated-data Python workflow passed a clean GitHub Actions execution test. Independent reconciliation against authoritative population or healthcare source files remains incomplete.

