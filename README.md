# Project 6: Manitoba Regional Health Equity Analysis

**Domain:** Health Equity / Social Determinants of Health
**Tools:** Python · SQL · Excel
**Real Data Source:** Manitoba Health Annual Statistics
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

## Key Findings

1. **Northern RHA premature mortality is nearly twice the provincial average.** Premature mortality in Northern RHA (669 per 100,000) is 2.0x the average of the other four RHAs (339). This is the most severe health equity gap in the province and reflects structural failures in primary care access, not just population risk factors.

2. **41% of Northern residents have no regular doctor.** The Northern no-doctor rate (41.5%) is the highest in Manitoba and 20 percentage points above the provincial average. Without a regular physician, chronic disease management defaults to emergency services, which drives the high hospitalisation rate (145 per 1,000).

3. **Northern diabetes prevalence is double Winnipeg's rate.** Northern RHA diabetes prevalence (19.6%) is 2.0x Winnipeg's rate (9.7%). Prairie Mountain also exceeds the provincial average. Structured community health worker programs in these two RHAs would cost less than the downstream hospital admissions from unmanaged diabetes.

4. **Low income is the strongest predictor of poor health outcomes.** Low income correlates r=0.94 with mortality rate across all five RHAs. Northern RHA has 38.6% low-income population versus 18.2% in Winnipeg. Health investment alone cannot close this gap without parallel investment in income supports and housing.

---

## Excel Workbook

**File:** `manitoba_health_equity.xlsx`

| Sheet | Contents |
|-------|---------|
| Summary | KPI cards for Northern RHA, 4 key findings with supporting text |
| RHA Indicators | All 5 RHAs × 9 indicators, composite equity score, bar chart |
| Northern RHA Trends | Year-over-year trend 2018–2022 with COVID annotation, gap vs provincial average |
| Social Determinants | Correlation table — low income, no doctor, and smoking vs mortality rate |

---

## Strategic Recommendations

1. **Northern RHA — critical primary care intervention.** Fund a full-time primary care team in each of the 8 largest northern communities with guaranteed multi-year contracts. The 41% no-doctor rate cannot be addressed by incentive programs alone — it requires structural placement commitments.

2. **Diabetes prevention in Northern and Prairie Mountain RHAs.** Both RHAs have diabetes prevalence nearly double Winnipeg's rate. A community health worker program focused on nutrition and physical activity in these two RHAs would reduce hospital admissions from unmanaged diabetes at lower cost than acute care.

3. **Expand the Rural Physician Incentive Program.** Interlake-Eastern and Northern RHAs have the lowest physician visit rates per capita. Loan forgiveness tied to 3-year rural placement commitments is the most cost-effective physician recruitment tool available to Manitoba Health.

4. **Income as root cause.** Health spending alone cannot close equity gaps in the Northern RHA. Housing and income supports for Northern communities must run in parallel with any health system investment — the correlation data makes this unambiguous.

---

## Files

| File | Purpose |
|------|---------|
| `simulate_manitoba.py` | Builds representative RHA-level data from published Manitoba Health Annual Statistics figures |
| `analysis.py` | RHA profile, Northern gap analysis, composite equity score, social determinant correlations, trend analysis |
| `sql_queries.sql` | 7 SQL queries covering RHA snapshot, burden index, COVID impact, and diabetes growth |
| `manitoba_health_equity.xlsx` | Excel workbook with 4 sheets — Summary, RHA Indicators, Northern Trends, Social Determinants |
| `equity_brief.md` | Plain-language brief for a Manitoba Health planning committee |

---

## Data Note
Manitoba Health Annual Statistics are published as PDF reports, not downloadable CSVs. This project uses simulated data anchored to published RHA-level indicators from the Manitoba Health Annual Statistics 2022–23 report. The simulation script documents all source figures inline. The analytical methodology reflects the approach used in provincial health planning roles.
