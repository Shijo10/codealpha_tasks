# ============================================================
# CODEALPHA INTERNSHIP — TASK 2: Exploratory Data Analysis
# Dataset: Titanic (built-in from seaborn)
# Author: CodeAlpha Intern
# ============================================================

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings('ignore')

# ─────────────────────────────────────────
# 1. LOAD DATASET
# ─────────────────────────────────────────
print("=" * 55)
print("   CODEALPHA — TASK 2: Exploratory Data Analysis")
print("   Dataset: Titanic")
print("=" * 55)

df = pd.read_csv('/home/claude/titanic.csv')
print(f"\n✅ Dataset loaded: {df.shape[0]} rows × {df.shape[1]} columns")

# ─────────────────────────────────────────
# 2. BASIC STRUCTURE
# ─────────────────────────────────────────
print("\n📌 STEP 1: Data Structure")
print("-" * 40)
print(df.dtypes)

print("\n📌 STEP 2: First 5 Rows")
print("-" * 40)
print(df.head())

# ─────────────────────────────────────────
# 3. MISSING VALUES
# ─────────────────────────────────────────
print("\n📌 STEP 3: Missing Values")
print("-" * 40)
missing = df.isnull().sum()
missing_pct = (df.isnull().sum() / len(df) * 100).round(2)
missing_df = pd.DataFrame({'Missing Count': missing, 'Missing %': missing_pct})
print(missing_df[missing_df['Missing Count'] > 0])

# ─────────────────────────────────────────
# 4. STATISTICAL SUMMARY
# ─────────────────────────────────────────
print("\n📌 STEP 4: Statistical Summary (Numerical)")
print("-" * 40)
print(df.describe().round(2))

print("\n📌 STEP 5: Categorical Summary")
print("-" * 40)
for col in ['sex', 'pclass', 'embarked']:
    print(f"\n  {col.upper()} value counts:")
    print(df[col].value_counts())

# ─────────────────────────────────────────
# 5. KEY QUESTIONS & ANALYSIS
# ─────────────────────────────────────────
print("\n📌 STEP 6: Key Questions & Insights")
print("-" * 40)

# Q1: Overall survival rate
survival_rate = df['survived'].mean() * 100
print(f"\n  Q1: Overall survival rate = {survival_rate:.1f}%")

# Q2: Survival by gender
print("\n  Q2: Survival rate by gender:")
print(df.groupby('sex')['survived'].mean().mul(100).round(1).to_string())

# Q3: Survival by class
print("\n  Q3: Survival rate by passenger class:")
print(df.groupby('pclass')['survived'].mean().mul(100).round(1).to_string())

# Q4: Age statistics by survival
print("\n  Q4: Average age of survivors vs non-survivors:")
print(df.groupby('survived')['age'].mean().round(1).rename({0: 'Did not survive', 1: 'Survived'}).to_string())

# Q5: Fare statistics
print(f"\n  Q5: Average fare = £{df['fare'].mean():.2f}, Median = £{df['fare'].median():.2f}")

# ─────────────────────────────────────────
# 6. CORRELATION MATRIX
# ─────────────────────────────────────────
print("\n📌 STEP 7: Correlation Analysis")
print("-" * 40)
numeric_cols = df[['survived', 'pclass', 'age', 'sibsp', 'parch', 'fare']]
corr = numeric_cols.corr().round(3)
print(corr)

print("\n✅ EDA Complete! Key findings:")
print("  • Women had significantly higher survival rates (~74%) vs men (~19%)")
print("  • 1st class passengers survived more (~63%) than 3rd class (~24%)")
print("  • Younger passengers had a slight survival advantage")
print("  • Fare is positively correlated with survival (wealthier → more likely to survive)")
print("\n  → Run task3_visualization.py to see all these insights as charts!\n")
