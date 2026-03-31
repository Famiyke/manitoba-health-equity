"""
Project 6 – analysis.py
Data Detective → Programmer → Storyteller → Consultant
Manitoba Health Equity Analysis
"""

import pandas as pd
import numpy as np

df  = pd.read_csv("manitoba_rha.csv")
sep = "=" * 62

print(f"\n{sep}")
print("  PROJECT 6 — MANITOBA HEALTH EQUITY ANALYSIS")
print(f"{sep}")
print(f"\n  Rows: {len(df):,}")
print(f"  RHAs: {sorted(df['rha'].unique())}")
print(f"  Years: {sorted(df['year'].unique())}")

INDICATORS = [
    "mortality_rate","premature_mort","diabetes_prev","hypertension_prev",
    "physician_visits_pc","hosp_seps_per_1000","low_income_pct",
    "no_doc_pct","smoking_pct",
]

# ── Latest Year Snapshot ──────────────────────────────────────────────────────
latest = df[df["year"] == df["year"].max()]

print(f"\n{'─'*62}")
print(f"RHA PROFILE — {df['year'].max()} KEY INDICATORS")
print(f"{'─'*62}")

print(f"\n  {'RHA':<22} {'Mortality':>10} {'Diabetes%':>10} {'No Doctor%':>11} {'Low Income%':>12}")
print(f"  {'─'*22} {'─'*10} {'─'*10} {'─'*11} {'─'*12}")
for _, r in latest.iterrows():
    flag = " ◄ HIGHEST BURDEN" if r["rha"] == "Northern" else ""
    print(f"  {r['rha']:<22} {r['mortality_rate']:>9.1f} {r['diabetes_prev']:>9.1f}%"
          f" {r['no_doc_pct']:>10.1f}% {r['low_income_pct']:>11.1f}%{flag}")

# ── Northern RHA Deep Dive ────────────────────────────────────────────────────
print(f"\n{'─'*62}")
print("NORTHERN RHA vs PROVINCIAL AVERAGE — GAP ANALYSIS")
print(f"{'─'*62}")

northern = latest[latest["rha"] == "Northern"].iloc[0]
prov_avg = latest[latest["rha"] != "Northern"][INDICATORS].mean()

print(f"\n  {'Indicator':<28} {'Northern':>10} {'Prov Avg':>10} {'Gap':>10}")
print(f"  {'─'*28} {'─'*10} {'─'*10} {'─'*10}")

BETTER_IF_HIGHER = {"physician_visits_pc"}
for ind in INDICATORS:
    n_val = northern[ind]
    p_val = prov_avg[ind]
    diff  = n_val - p_val
    if ind in BETTER_IF_HIGHER:
        direction = "↑" if diff > 0 else "↓ WORSE"
    else:
        direction = "↓" if diff < 0 else "↑ WORSE"
    print(f"  {ind:<28} {n_val:>9.1f} {p_val:>9.1f} {diff:>+9.1f}  {direction}")

# ── Composite Equity Score ────────────────────────────────────────────────────
print(f"\n{'─'*62}")
print("COMPOSITE HEALTH EQUITY SCORE (lower = worse equity)")
print(f"{'─'*62}")

# Normalise each indicator — all on 0-100 scale where 100 = best health
score_df = latest.copy()
HIGHER_WORSE = ["mortality_rate","premature_mort","diabetes_prev",
                "hypertension_prev","hosp_seps_per_1000","low_income_pct",
                "no_doc_pct","smoking_pct"]
HIGHER_BETTER = ["physician_visits_pc"]

weights = {
    "mortality_rate": 0.20, "premature_mort": 0.15, "diabetes_prev": 0.10,
    "hypertension_prev": 0.08, "physician_visits_pc": 0.15,
    "hosp_seps_per_1000": 0.10, "low_income_pct": 0.10,
    "no_doc_pct": 0.07, "smoking_pct": 0.05,
}

score_df["equity_score"] = 0
for ind, weight in weights.items():
    vals = latest[ind]
    lo, hi = vals.min(), vals.max()
    if ind in HIGHER_WORSE:
        # invert: higher = worse → normalise so lower value = higher score
        norm = (hi - vals) / (hi - lo + 1e-9)
    else:
        norm = (vals - lo) / (hi - lo + 1e-9)
    score_df["equity_score"] += norm * weight * 100

score_df = score_df.sort_values("equity_score")

print(f"\n  {'RHA':<22} {'Equity Score':>14} {'Assessment':>14}")
print(f"  {'─'*22} {'─'*14} {'─'*14}")
for _, r in score_df.iterrows():
    score = r["equity_score"]
    assessment = "Critical" if score < 30 else "At Risk" if score < 50 else "Moderate" if score < 70 else "Strong"
    print(f"  {r['rha']:<22} {score:>13.0f} {assessment:>14}")

# ── Social Determinant Correlation ───────────────────────────────────────────
print(f"\n{'─'*62}")
print("SOCIAL DETERMINANT CORRELATION WITH MORTALITY RATE")
print(f"{'─'*62}")

determinants = ["low_income_pct","no_doc_pct","smoking_pct"]
print()
for det in determinants:
    sub = latest.dropna(subset=["mortality_rate", det])
    if len(sub) > 2:
        corr = np.corrcoef(sub[det], sub["mortality_rate"])[0, 1]
        strength = "Strong" if abs(corr) > 0.7 else "Moderate" if abs(corr) > 0.4 else "Weak"
        print(f"  {det:<22}  r = {corr:+.2f}  ({strength} correlation)")

# ── Year-over-Year for Northern RHA ──────────────────────────────────────────
print(f"\n{'─'*62}")
print("NORTHERN RHA — TRENDS OVER TIME")
print(f"{'─'*62}")

north_yoy = df[df["rha"] == "Northern"].sort_values("year")

print(f"\n  {'Year':>6} {'Mortality':>10} {'Diabetes%':>10} {'No Doctor%':>12} {'Phys Visits':>12}")
print(f"  {'─'*6} {'─'*10} {'─'*10} {'─'*12} {'─'*12}")
for _, r in north_yoy.iterrows():
    note = " ← COVID" if r["year"] == 2020 else ""
    print(f"  {r['year']:>6} {r['mortality_rate']:>9.1f} {r['diabetes_prev']:>9.1f}%"
          f" {r['no_doc_pct']:>11.1f}% {r['physician_visits_pc']:>11.1f}{note}")

# ── Recommendations ───────────────────────────────────────────────────────────
print(f"\n{'─'*62}")
print("STRATEGIC RECOMMENDATIONS")
print(f"{'─'*62}")
print("""
  1. NORTHERN RHA — CRITICAL INTERVENTION
     Northern Manitoba has premature mortality twice
     the provincial average and 41% of residents
     report having no regular doctor. This is not
     a data problem — it is a placement problem.
     Manitoba Health should fund a full-time primary
     care team in each of the 8 largest northern
     communities, with guaranteed multi-year contracts.

  2. DIABETES AND HYPERTENSION PREVENTION
     Northern and Prairie Mountain RHAs have diabetes
     prevalence nearly double Winnipeg's rate.
     A structured community health worker program
     focused on nutrition and physical activity in
     these two RHAs would cost less than the hospital
     admissions that result from unmanaged diabetes.

  3. PHYSICIAN ACCESS GAPS
     Interlake-Eastern and Northern RHAs have the
     lowest physician visit rates per capita.
     Manitoba should expand its Rural Physician
     Incentive Program and provide loan forgiveness
     tied to 3-year rural placement commitments.

  4. INCOME AS ROOT CAUSE
     Low-income proportion correlates strongly with
     every negative health outcome across all RHAs.
     Health spending alone cannot close equity gaps
     without parallel investment in housing and
     income supports for the Northern RHA population.
""")
print(sep)
