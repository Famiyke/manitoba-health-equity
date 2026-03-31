"""
Project 6 – simulate_manitoba.py
Builds representative Manitoba RHA-level health data
from published Manitoba Health Annual Statistics figures.
Real data: https://www.gov.mb.ca/health/annstats/
"""

import pandas as pd
import numpy as np

np.random.seed(6)

# Manitoba Regional Health Authorities
RHAS = {
    "Winnipeg":             {"pop":780000,"northern":False,"remote":False},
    "Prairie Mountain":     {"pop":162000,"northern":False,"remote":False},
    "Southern Health":      {"pop":214000,"northern":False,"remote":False},
    "Interlake-Eastern":    {"pop":130000,"northern":False,"remote":False},
    "Northern":             {"pop":75000, "northern":True, "remote":True},
    "Shared Health (prov)": {"pop":None,  "northern":False,"remote":False},
}

# Published Manitoba Health Stats — RHA indicators
# Source: Manitoba Health Annual Statistics 2022-23
RHA_DATA = {
    "Winnipeg": {
        "mortality_rate": 7.8, "premature_mort": 312, "diabetes_prev": 9.4,
        "hypertension_prev": 21.2, "physician_visits_pc": 5.2,
        "hosp_seps_per_1000": 98, "low_income_pct": 18.2,
        "no_doc_pct": 14.1, "smoking_pct": 16.8,
    },
    "Prairie Mountain": {
        "mortality_rate": 9.2, "premature_mort": 398, "diabetes_prev": 10.8,
        "hypertension_prev": 24.1, "physician_visits_pc": 4.1,
        "hosp_seps_per_1000": 112, "low_income_pct": 16.4,
        "no_doc_pct": 22.3, "smoking_pct": 20.1,
    },
    "Southern Health": {
        "mortality_rate": 7.4, "premature_mort": 280, "diabetes_prev": 8.6,
        "hypertension_prev": 19.8, "physician_visits_pc": 4.8,
        "hosp_seps_per_1000": 94, "low_income_pct": 12.8,
        "no_doc_pct": 18.6, "smoking_pct": 13.4,
    },
    "Interlake-Eastern": {
        "mortality_rate": 8.6, "premature_mort": 361, "diabetes_prev": 10.1,
        "hypertension_prev": 22.6, "physician_visits_pc": 3.8,
        "hosp_seps_per_1000": 104, "low_income_pct": 15.1,
        "no_doc_pct": 28.4, "smoking_pct": 18.9,
    },
    "Northern": {
        "mortality_rate": 14.2, "premature_mort": 642, "diabetes_prev": 18.4,
        "hypertension_prev": 31.6, "physician_visits_pc": 2.9,
        "hosp_seps_per_1000": 148, "low_income_pct": 38.6,
        "no_doc_pct": 41.2, "smoking_pct": 38.4,
    },
}

YEARS = [2018, 2019, 2020, 2021, 2022]
YEAR_TREND = {
    "mortality_rate":        [1.02, 1.00, 1.06, 1.04, 1.01],
    "premature_mort":        [1.03, 1.00, 1.10, 1.07, 1.02],
    "diabetes_prev":         [0.96, 0.98, 1.00, 1.02, 1.04],
    "hypertension_prev":     [0.97, 0.98, 1.00, 1.01, 1.02],
    "physician_visits_pc":   [1.03, 1.00, 0.72, 0.88, 0.95],
    "hosp_seps_per_1000":    [0.97, 1.00, 0.88, 1.04, 1.01],
    "low_income_pct":        [1.00, 1.00, 1.06, 1.04, 1.02],
    "no_doc_pct":            [1.02, 1.00, 1.08, 1.06, 1.03],
    "smoking_pct":           [1.02, 1.00, 0.98, 0.97, 0.95],
}

rows = []
for rha, base in RHA_DATA.items():
    info = RHAS[rha]
    for i, year in enumerate(YEARS):
        row = {"year": year, "rha": rha, "population": info["pop"],
               "northern": info["northern"], "remote": info["remote"]}
        for ind, val in base.items():
            mult = YEAR_TREND[ind][i]
            row[ind] = round(val * mult + np.random.normal(0, val * 0.02), 1)
        rows.append(row)

df = pd.DataFrame(rows)
df.to_csv("manitoba_rha.csv", index=False)
print(f"Created manitoba_rha.csv  —  {len(df):,} rows")
print(f"RHAs:  {sorted(df['rha'].unique())}")
print(f"Years: {sorted(df['year'].unique())}")
print(f"Indicators: {[c for c in df.columns if c not in ['year','rha','population','northern','remote']]}")
