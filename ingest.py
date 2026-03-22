import sys
import pandas as pd
import subprocess

# check if dataset path is provided
if len(sys.argv) < 2:
    print("Usage: python ingest.py <dataset_path>")
    sys.exit(1)

# get dataset path from command line
dataset_path = sys.argv[1]

try:
    # read dataset (important: separator is ;)
    df = pd.read_csv(dataset_path, sep=';')
except Exception as e:
    print(f"Error reading dataset: {e}")
    sys.exit(1)

# save raw copy
df.to_csv("data_raw.csv", index=False)

print("Raw data saved as data_raw.csv")

# call preprocess script and pass new file
subprocess.run(["python", "preprocess.py", "data_raw.csv"])