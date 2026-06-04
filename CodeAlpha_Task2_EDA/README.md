# 📊 Task 2 — Exploratory Data Analysis (EDA)

![Python](https://img.shields.io/badge/Python-3.8+-blue?style=flat-square&logo=python)
![Pandas](https://img.shields.io/badge/Pandas-1.x-150458?style=flat-square&logo=pandas)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen?style=flat-square)

> **CodeAlpha Data Analytics Internship — Task 2**

---

## 📌 Objective

Perform a thorough Exploratory Data Analysis (EDA) on the **Titanic dataset** to:
- Understand the data structure and variable types
- Identify missing values and anomalies
- Derive statistical summaries
- Answer key analytical questions about passenger survival
- Detect correlations between features

---

## 📂 Files

| File | Description |
|---|---|
| `task2_eda.py` | Main Python script for EDA |
| `titanic.csv` | Titanic passenger dataset (891 rows × 8 columns) |
| `README.md` | Task documentation |

---

## 🗃️ Dataset Overview

| Column | Type | Description |
|---|---|---|
| `survived` | int | 0 = No, 1 = Yes |
| `pclass` | int | Passenger class (1, 2, 3) |
| `sex` | str | Gender |
| `age` | float | Age (19.5% missing) |
| `sibsp` | int | Siblings/Spouses aboard |
| `parch` | int | Parents/Children aboard |
| `fare` | float | Ticket fare (£) |
| `embarked` | str | Port: S=Southampton, C=Cherbourg, Q=Queenstown |

---

## 🔍 Analysis Steps

1. **Data Loading** — Load CSV and inspect shape
2. **Data Structure** — Check dtypes and column names
3. **Missing Values** — Identify and quantify nulls
4. **Statistical Summary** — Describe numerical features
5. **Categorical Summary** — Value counts for sex, class, port
6. **Key Questions** — Survival rates by gender, class, age
7. **Correlation Matrix** — Feature relationships with survival

---

## 📈 Key Findings

| Insight | Value |
|---|---|
| Overall survival rate | **52.4%** |
| Female survival rate | **72.7%** |
| Male survival rate | **40.7%** |
| 1st Class survival | **78.6%** |
| 3rd Class survival | **37.7%** |
| Average fare (survivors) | Higher than non-survivors |
| Fare–Survival correlation | **+0.227** |

---

## ⚙️ How to Run

```bash
# Install dependencies
pip install pandas numpy matplotlib seaborn

# Run the EDA script
python task2_eda.py
```

---

## 🧠 Conclusions

- **Gender** was the strongest survival predictor — women were prioritized during evacuation
- **Passenger class** heavily influenced survival — wealth and cabin location mattered
- **Age** had a slight negative correlation — younger passengers fared marginally better
- **Fare** positively correlated with survival, reflecting class-based advantages

---

> 📁 Part of [CodeAlpha_DataAnalytics](../README.md) repository
