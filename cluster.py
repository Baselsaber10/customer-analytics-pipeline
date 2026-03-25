import pandas as pd
from sklearn.cluster import KMeans
import sys

# -----------------------------
# Check input
# -----------------------------
if len(sys.argv) < 2:
    print("Usage: python cluster.py <input_csv>")
    sys.exit(1)

# -----------------------------
# Load data
# -----------------------------
file_path = sys.argv[1]
df = pd.read_csv(file_path)

# -----------------------------
# Select features
# -----------------------------
features = ['age', 'balance', 'duration']
X = df[features].dropna()

print("Using features:", features)

# -----------------------------
# Apply K-Means
# -----------------------------
kmeans = KMeans(n_clusters=3, random_state=42)
df['cluster'] = kmeans.fit_predict(X)

# -----------------------------
# Output cluster counts
# -----------------------------
cluster_counts = df['cluster'].value_counts().sort_index()

with open("clusters.txt", "w") as f:
    for cluster_id, count in cluster_counts.items():
        f.write(f"Cluster {cluster_id}: {count} samples\n")

print("Clustering completed. Cluster counts saved in clusters.txt")


print("Cluster centers:")
print(kmeans.cluster_centers_)