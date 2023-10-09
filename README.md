# Week 6 Mini Project [![CI](https://github.com/nogibjj/Gavin_Li_Week6_Mini_Project/actions/workflows/cicd.yml/badge.svg)](https://github.com/nogibjj/Gavin_Li_Week6_Mini_Project/actions/workflows/cicd.yml)

Gavin Li `gl183`

## Purpose of the project

The purpose of this week's mini project is to connect to database using python scripts, and manipulate database using python scripts.

## Result for `make test` and `make lint`

![make_rslt](./resources/make_test_lint.png)

## CRUD result and `make query`
![CRUD_rlst](./resources/CRUD_rslt.png)

## A flow chart demonstrating the workflow
![flow_chart](./resources/flow_chart.png)


```sql
SELECT
    state_abbrevs.state,
    SUM(total) AS total_crimes
FROM us_crime
JOIN state_abbrevs
ON us_crime.state = state_abbrevs.abbrev
GROUP BY state_abbrevs.state
ORDER BY total_crimes DESC;
```