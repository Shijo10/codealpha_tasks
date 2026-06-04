# ============================================================
# CODEALPHA INTERNSHIP — TASK 3: Data Visualization
# Dataset: Titanic (built-in from seaborn)
# Author: CodeAlpha Intern
# ============================================================

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import warnings
warnings.filterwarnings('ignore')

# ─────────────────────────────────────────
# SETUP
# ─────────────────────────────────────────
df = pd.read_csv('/home/claude/titanic.csv')

# Clean data for visualizations
df['age'].fillna(df['age'].median(), inplace=True)
df['embarked'].fillna(df['embarked'].mode()[0], inplace=True)
df['sex_label'] = df['sex'].map({'male': 'Male', 'female': 'Female'})
df['survived_label'] = df['survived'].map({0: 'Did Not Survive', 1: 'Survived'})
df['pclass_label'] = df['pclass'].map({1: '1st Class', 2: '2nd Class', 3: '3rd Class'})

# Color palette
COLORS = ['#E74C3C', '#2ECC71']
PALETTE = {'Did Not Survive': '#E74C3C', 'Survived': '#2ECC71'}
BG = '#1A1A2E'
CARD = '#16213E'
TEXT = '#EAEAEA'

plt.rcParams.update({
    'figure.facecolor': BG,
    'axes.facecolor': CARD,
    'axes.edgecolor': '#2C3E50',
    'axes.labelcolor': TEXT,
    'xtick.color': TEXT,
    'ytick.color': TEXT,
    'text.color': TEXT,
    'grid.color': '#2C3E50',
    'grid.linewidth': 0.5,
    'font.family': 'DejaVu Sans',
})

print("=" * 55)
print("   CODEALPHA — TASK 3: Data Visualization")
print("   Dataset: Titanic")
print("=" * 55)
print("\n📊 Generating 6-panel dashboard...\n")

# ─────────────────────────────────────────
# DASHBOARD: 6 CHARTS
# ─────────────────────────────────────────
fig = plt.figure(figsize=(18, 12), facecolor=BG)
fig.suptitle('🚢  Titanic Survival Analysis Dashboard',
             fontsize=22, fontweight='bold', color=TEXT, y=0.98)

# ── Chart 1: Overall Survival (Pie) ─────
ax1 = fig.add_subplot(2, 3, 1)
survival_counts = df['survived_label'].value_counts()
wedges, texts, autotexts = ax1.pie(
    survival_counts,
    labels=survival_counts.index,
    autopct='%1.1f%%',
    colors=COLORS,
    startangle=90,
    wedgeprops={'edgecolor': BG, 'linewidth': 2},
    textprops={'color': TEXT, 'fontsize': 11}
)
for at in autotexts:
    at.set_fontsize(12)
    at.set_fontweight('bold')
ax1.set_title('Overall Survival Rate', fontsize=13, fontweight='bold', pad=12)

# ── Chart 2: Survival by Gender (Bar) ───
ax2 = fig.add_subplot(2, 3, 2)
gender_survival = df.groupby(['sex_label', 'survived_label']).size().reset_index(name='count')
pivot = gender_survival.pivot(index='sex_label', columns='survived_label', values='count')
pivot.plot(kind='bar', ax=ax2, color=COLORS, edgecolor=BG, linewidth=1.5, width=0.6)
ax2.set_title('Survival by Gender', fontsize=13, fontweight='bold')
ax2.set_xlabel('Gender', fontsize=11)
ax2.set_ylabel('Passengers', fontsize=11)
ax2.set_xticklabels(ax2.get_xticklabels(), rotation=0, fontsize=11)
ax2.legend(title='', fontsize=9, facecolor=CARD, edgecolor='#2C3E50', labelcolor=TEXT)
ax2.grid(axis='y', alpha=0.4)

# ── Chart 3: Survival by Class (Bar) ────
ax3 = fig.add_subplot(2, 3, 3)
class_survival = df.groupby('pclass_label')['survived'].mean().mul(100)
bars = ax3.bar(class_survival.index, class_survival.values,
               color=['#F39C12', '#3498DB', '#9B59B6'], edgecolor=BG, linewidth=1.5)
for bar, val in zip(bars, class_survival.values):
    ax3.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 1,
             f'{val:.1f}%', ha='center', va='bottom', fontsize=11, fontweight='bold', color=TEXT)
ax3.set_title('Survival Rate by Passenger Class', fontsize=13, fontweight='bold')
ax3.set_xlabel('Passenger Class', fontsize=11)
ax3.set_ylabel('Survival Rate (%)', fontsize=11)
ax3.set_ylim(0, 80)
ax3.grid(axis='y', alpha=0.4)

# ── Chart 4: Age Distribution (Histogram) ─
ax4 = fig.add_subplot(2, 3, 4)
survived = df[df['survived'] == 1]['age']
not_survived = df[df['survived'] == 0]['age']
ax4.hist(not_survived, bins=30, alpha=0.7, color='#E74C3C', label='Did Not Survive', edgecolor=BG)
ax4.hist(survived, bins=30, alpha=0.7, color='#2ECC71', label='Survived', edgecolor=BG)
ax4.axvline(survived.mean(), color='#2ECC71', linestyle='--', linewidth=1.5, label=f'Survivor Avg: {survived.mean():.1f}')
ax4.axvline(not_survived.mean(), color='#E74C3C', linestyle='--', linewidth=1.5, label=f'Non-survivor Avg: {not_survived.mean():.1f}')
ax4.set_title('Age Distribution by Survival', fontsize=13, fontweight='bold')
ax4.set_xlabel('Age', fontsize=11)
ax4.set_ylabel('Count', fontsize=11)
ax4.legend(fontsize=8, facecolor=CARD, edgecolor='#2C3E50', labelcolor=TEXT)
ax4.grid(axis='y', alpha=0.4)

# ── Chart 5: Fare vs Age (Scatter) ──────
ax5 = fig.add_subplot(2, 3, 5)
for label, color in PALETTE.items():
    mask = df['survived_label'] == label
    ax5.scatter(df[mask]['age'], df[mask]['fare'],
                alpha=0.5, c=color, s=25, label=label, edgecolors='none')
ax5.set_title('Fare vs Age (by Survival)', fontsize=13, fontweight='bold')
ax5.set_xlabel('Age', fontsize=11)
ax5.set_ylabel('Fare (£)', fontsize=11)
ax5.set_ylim(0, 300)
ax5.legend(fontsize=9, facecolor=CARD, edgecolor='#2C3E50', labelcolor=TEXT)
ax5.grid(alpha=0.3)

# ── Chart 6: Survival by Embarkation ────
ax6 = fig.add_subplot(2, 3, 6)
embark_map = {'S': 'Southampton', 'C': 'Cherbourg', 'Q': 'Queenstown'}
df['embark_label'] = df['embarked'].map(embark_map)
embark_surv = df.groupby('embark_label')['survived'].mean().mul(100).sort_values(ascending=True)
colors_emb = ['#E67E22', '#1ABC9C', '#3498DB']
bars = ax6.barh(embark_surv.index, embark_surv.values,
                color=colors_emb, edgecolor=BG, linewidth=1.5)
for bar, val in zip(bars, embark_surv.values):
    ax6.text(val + 0.5, bar.get_y() + bar.get_height() / 2,
             f'{val:.1f}%', va='center', fontsize=11, fontweight='bold', color=TEXT)
ax6.set_title('Survival Rate by Embarkation Port', fontsize=13, fontweight='bold')
ax6.set_xlabel('Survival Rate (%)', fontsize=11)
ax6.set_xlim(0, 65)
ax6.grid(axis='x', alpha=0.4)

# ─────────────────────────────────────────
plt.tight_layout(rect=[0, 0, 1, 0.96])
output_path = '/mnt/user-data/outputs/titanic_dashboard.png'
plt.savefig(output_path, dpi=180, bbox_inches='tight', facecolor=BG)
print(f"✅ Dashboard saved to: {output_path}")
plt.show()

print("\n📌 Visual Insights:")
print("  1. Only 38% of passengers survived the disaster")
print("  2. Female survival rate (~74%) was far higher than males (~19%)")
print("  3. 1st class passengers had the highest survival rate (~63%)")
print("  4. Children and younger passengers showed slightly higher survival")
print("  5. Higher fare payers (wealthier) were more likely to survive")
print("  6. Cherbourg passengers had the highest survival rate (~55%)")
print("\n✅ Task 3 Complete!\n")
