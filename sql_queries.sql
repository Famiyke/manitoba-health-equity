-- Project 6: Manitoba Health Equity Analysis
-- sql_queries.sql  —  SQL Programmer Hat
-- Load manitoba_rha.csv as table: manitoba

-- ── 1. RHA snapshot — latest year ────────────────────────────────────────────
SELECT
    rha,
    ROUND(mortality_rate, 1)         AS mortality_rate,
    ROUND(premature_mort, 0)         AS premature_mort,
    ROUND(diabetes_prev, 1)          AS diabetes_pct,
    ROUND(no_doc_pct, 1)             AS no_doctor_pct,
    ROUND(low_income_pct, 1)         AS low_income_pct,
    ROUND(physician_visits_pc, 1)    AS physician_visits_pc
FROM manitoba
WHERE year = (SELECT MAX(year) FROM manitoba)
ORDER BY mortality_rate DESC;

-- ── 2. Northern vs. all others ────────────────────────────────────────────────
SELECT
    CASE WHEN northern = 1 THEN 'Northern' ELSE 'Southern/Urban' END AS region_type,
    ROUND(AVG(mortality_rate), 1)    AS avg_mortality,
    ROUND(AVG(premature_mort), 0)    AS avg_premature_mort,
    ROUND(AVG(diabetes_prev), 1)     AS avg_diabetes_pct,
    ROUND(AVG(no_doc_pct), 1)        AS avg_no_doctor_pct,
    ROUND(AVG(low_income_pct), 1)    AS avg_low_income_pct,
    ROUND(AVG(physician_visits_pc),1) AS avg_physician_visits
FROM manitoba
WHERE year = (SELECT MAX(year) FROM manitoba)
GROUP BY region_type;

-- ── 3. Year-over-year mortality trend by RHA ──────────────────────────────────
SELECT
    rha,
    year,
    ROUND(mortality_rate, 1)          AS mortality_rate,
    ROUND(premature_mort, 0)          AS premature_mortality
FROM manitoba
ORDER BY rha, year;

-- ── 4. Composite burden index ─────────────────────────────────────────────────
-- Weight: mortality 30%, diabetes 20%, no doctor 25%, low income 25%
SELECT
    rha,
    ROUND(
        mortality_rate   * 0.30 +
        diabetes_prev    * 0.20 +
        no_doc_pct       * 0.25 +
        low_income_pct   * 0.25
    , 1)                              AS burden_index,
    ROUND(mortality_rate, 1)          AS mortality,
    ROUND(diabetes_prev, 1)           AS diabetes_pct,
    ROUND(no_doc_pct, 1)              AS no_doc_pct,
    ROUND(low_income_pct, 1)          AS low_income_pct
FROM manitoba
WHERE year = (SELECT MAX(year) FROM manitoba)
ORDER BY burden_index DESC;

-- ── 5. Low income and health outcomes correlation ─────────────────────────────
SELECT
    rha,
    ROUND(low_income_pct, 1)    AS low_income_pct,
    ROUND(mortality_rate, 1)    AS mortality_rate,
    ROUND(no_doc_pct, 1)        AS no_doc_pct,
    ROUND(diabetes_prev, 1)     AS diabetes_pct
FROM manitoba
WHERE year = (SELECT MAX(year) FROM manitoba)
ORDER BY low_income_pct DESC;

-- ── 6. COVID impact — physician visits ───────────────────────────────────────
SELECT
    year,
    rha,
    ROUND(physician_visits_pc, 1)   AS physician_visits_pc
FROM manitoba
WHERE year IN (2019, 2020, 2021, 2022)
ORDER BY rha, year;

-- ── 7. Diabetes and hypertension growth ──────────────────────────────────────
SELECT
    rha,
    ROUND(AVG(CASE WHEN year = (SELECT MIN(year) FROM manitoba)
                   THEN diabetes_prev END), 1) AS diabetes_earliest,
    ROUND(AVG(CASE WHEN year = (SELECT MAX(year) FROM manitoba)
                   THEN diabetes_prev END), 1) AS diabetes_latest,
    ROUND(
        (AVG(CASE WHEN year = (SELECT MAX(year) FROM manitoba)
                  THEN diabetes_prev END)
       - AVG(CASE WHEN year = (SELECT MIN(year) FROM manitoba)
                  THEN diabetes_prev END))
       / AVG(CASE WHEN year = (SELECT MIN(year) FROM manitoba)
                  THEN diabetes_prev END) * 100
    , 1)                                        AS pct_growth
FROM manitoba
GROUP BY rha
ORDER BY pct_growth DESC;
