import sys
import pandas as pd

# Check input
if len(sys.argv) < 2:
    print("Usage: python analytics.py <input_csv>")
    sys.exit(1)

# Load data
df = pd.read_csv(sys.argv[1])

# =========================
# Insight 1: Call Duration Impact
# =========================
if "duration" in df.columns and "y" in df.columns:
    duration_yes = df[df["y"] == 1]["duration"].mean()
    duration_no = df[df["y"] == 0]["duration"].mean()

    with open("insight1.txt", "w") as f:
        f.write(f"Average call duration for subscribers: {duration_yes:.2f}\n")
        f.write(f"Average call duration for non-subscribers: {duration_no:.2f}\n")
        f.write(f"Subscribers have {(duration_yes/duration_no)*100:.1f}% longer calls\n")

# =========================
# Insight 2: Overall Subscription Rate
# =========================
if "y" in df.columns:
    rate = df["y"].mean() * 100

    with open("insight2.txt", "w") as f:
        f.write(f"Overall subscription rate: {rate:.2f}%\n")

# =========================
# Insight 3: Age Group Analysis
# =========================
if "age" in df.columns and "y" in df.columns:
    df["age_group"] = pd.cut(
        df["age"],
        bins=[-3, -1, 0, 1, 3],  # because age is scaled now
        labels=["young", "adult", "middle", "senior"]
    )

    subscription_by_age = df.groupby("age_group")["y"].mean() * 100

    with open("insight3.txt", "w") as f:
        f.write("Subscription rate by age group:\n")
        f.write(str(subscription_by_age.round(2)))

print("Insights generated successfully.")
#import subprocess
#subprocess.run(["python", "visualize.py", sys.argv[1]])