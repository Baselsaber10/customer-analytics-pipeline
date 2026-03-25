import sys
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler

# Check input argument
if len(sys.argv) < 2:
    print("Usage: python preprocess.py <input_csv>")
    sys.exit(1)

# Load dataset
try:
    bank_data = pd.read_csv(sys.argv[1], sep=';')
except Exception as e:
    print(f"Error reading input file: {e}")
    sys.exit(1)

# Display basic information
print("Original data info:")
bank_data.info()

# =========================
# 1. Data Cleaning
# =========================

# Remove duplicate rows
bank_data.drop_duplicates(inplace=True)

# Replace 'unknown' with NaN in selected categorical columns
bank_data['job'] = bank_data['job'].replace('unknown', np.nan)
bank_data['education'] = bank_data['education'].replace('unknown', np.nan)
bank_data['contact'] = bank_data['contact'].replace('unknown', np.nan)
bank_data['poutcome'] = bank_data['poutcome'].replace('unknown', np.nan)

# Replace -1 in pdays with NaN
bank_data['pdays'] = bank_data['pdays'].replace(-1, np.nan)

# Fill missing categorical values with mode
bank_data['job'] = bank_data['job'].fillna(bank_data['job'].mode()[0])
bank_data['education'] = bank_data['education'].fillna(bank_data['education'].mode()[0])
bank_data['contact'] = bank_data['contact'].fillna(bank_data['contact'].mode()[0])
bank_data['poutcome'] = bank_data['poutcome'].fillna(bank_data['poutcome'].mode()[0])

# Fill missing numeric values with median
bank_data['pdays'] = bank_data['pdays'].fillna(bank_data['pdays'].median())

# =========================
# 2. Discretization
# =========================

# Bin age into groups
bank_data['age_group'] = pd.cut(
    bank_data['age'],
    bins=[0, 30, 45, 60, 100],
    labels=['young', 'adult', 'middle_aged', 'senior'],
    include_lowest=True
)

# Bin balance into groups
bank_data['balance_group'] = pd.cut(
    bank_data['balance'],
    bins=[-100000, 0, 2000, 1000000],
    labels=['low', 'medium', 'high'],
    include_lowest=True
)

# Bin duration into groups
bank_data['duration_group'] = pd.cut(
    bank_data['duration'],
    bins=[0, 120, 300, 5000],
    labels=['short', 'medium', 'long'],
    include_lowest=True
)

# =========================
# 3. Feature Transformation
# =========================

# Convert target column to numeric
bank_data['y'] = bank_data['y'].map({'yes': 1, 'no': 0})

# One-hot encoding 
bank_data = pd.get_dummies(
    bank_data,
    columns=[
        'job', 'marital', 'education', 'default', 'housing', 'loan',
        'contact', 'month', 'poutcome',
        'age_group', 'balance_group', 'duration_group'
    ],
    drop_first=True
)

# Convert boolean columns to 0/1
bool_cols = bank_data.select_dtypes(include='bool').columns
bank_data[bool_cols] = bank_data[bool_cols].astype(int)

# Scale numeric columns
scaler = StandardScaler()
numeric_cols = ['age', 'balance', 'day', 'duration', 'campaign', 'pdays', 'previous']
bank_data[numeric_cols] = scaler.fit_transform(bank_data[numeric_cols])

# =========================
# 4. Dimensionality Reduction
# =========================

# Keep only selected useful columns
selected_columns = [
    col for col in bank_data.columns if
    'age' in col or
    'balance' in col or
    'duration' in col or
    'campaign' in col or
    'pdays' in col or
    'previous' in col or
    'housing' in col or
    'loan' in col or
    'job' in col or
    'marital' in col or
    col == 'y'
]

bank_data = bank_data[selected_columns]

# Save preprocessed data
bank_data.to_csv("data_preprocessed.csv", index=False)

print("\nPreprocessing completed successfully.")
print("Preprocessed data saved as data_preprocessed.csv")
print("\nProcessed data info:")
bank_data.info()