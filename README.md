# Project 6: Manitoba Health Equity Analysis

**Domain:** Health Equity / Social Determinants of Health  
**Tools:** Python · SQL · Excel · Power BI  
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
3. Open in Adobe or browser — find tables for:
   - Mortality by RHA and cause
   - Physician visits per capita by RHA
   - Hospital separations by RHA
   - Diabetes and hypertension prevalence by RHA
4. Copy table values manually into the Excel template (`manitoba_rha_data.xlsx`)
5. Then run `python analysis.py` — it reads from the CSV export of your Excel

## How to Run (demo mode)
```bash
pip install pandas numpy openpyxl
python simulate_manitoba.py   # creates manitoba_rha.csv
python analysis.py            # full analysis
```

---

## Analyst Roles

| Hat | What I Did |
|-----|-----------|
| Data Detective | Extracted 6 indicator tables from Manitoba Health PDF, standardised RHA names, validated totals against provincial aggregates |
| SQL/Python Programmer | Ranked RHAs on composite health equity score, correlated indicators with social determinants |
| Dashboard Architect | Built Excel workbook with RHA comparison charts and equity score tracker |
| Data Storyteller | Produced a plain-language brief for a Manitoba Health committee |
| Strategic Consultant | Recommended three place-based investments for the highest-burden RHAs |
