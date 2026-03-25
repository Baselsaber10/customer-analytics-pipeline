import sys
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import subprocess

# -----------------------------
# Load data
# -----------------------------
if len(sys.argv) < 2:
    print("Usage: python visualize.py <input_csv>")
    sys.exit(1)

file_path = sys.argv[1]
df = pd.read_csv(file_path)

print("Creating visualizations...")

# -----------------------------
# Create figure: 2 rows, 2 columns
# -----------------------------
fig, axes = plt.subplots(2, 2, figsize=(14, 10))

# Flatten axes for easy indexing
axes = axes.flatten()

# 1. Histogram: Age
axes[0].hist(df['age'], bins=30, color='skyblue', edgecolor='black')
axes[0].set_title("Age Distribution")
axes[0].set_xlabel("Age")
axes[0].set_ylabel("Count")

# 2. Correlation Heatmap
sns.heatmap(df[['age','balance','duration','campaign','pdays','previous','y']].corr(),
            annot=True, cmap='coolwarm', vmin=-1, vmax=1, ax=axes[1])
axes[1].set_title("Correlation Heatmap")

# 3. Boxplot: Balance vs y
sns.boxplot(x='y', y='balance', data=df, palette='pastel', ax=axes[2])
axes[2].set_title("Balance by Subscription (y)")

# 4. Boxplot: Duration vs y
sns.boxplot(x='y', y='duration', data=df, palette='pastel', ax=axes[3])
axes[3].set_title("Call Duration by Subscription (y)")

# -----------------------------
# Adjust layout: center plots nicely
# -----------------------------
plt.tight_layout()
plt.savefig("summary_plot.png")
subprocess.run(["python", "cluster.py", file_path])