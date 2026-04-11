# Import required libraries
import pandas as pd
import numpy as np

from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt

# -------------------------------
# Step 1: Load Dataset
# -------------------------------

df = pd.read_csv("student.csv")

# -------------------------------
# Step 2: Select Required Features
# -------------------------------

features = [
    "StudyHours",
    "Attendance",
    "PreviousScore",
    "AssignmentsCompleted",
    "SleepHours"
]

data = df[features]

# -------------------------------
# Step 3: Data Preprocessing
# -------------------------------

data = data.dropna()

scaler = StandardScaler()
scaled_data = scaler.fit_transform(data)

# -------------------------------
# Step 4: Apply K-Means Clustering
# -------------------------------

kmeans = KMeans(n_clusters=3, random_state=42)

kmeans.fit(scaled_data)

data["Cluster"] = kmeans.labels_

# -------------------------------
# Step 5: Analyze Clusters
# -------------------------------

print("\nCluster-wise Mean Values:\n")
print(data.groupby("Cluster").mean())

# -------------------------------
# Step 6: Interpret Clusters
# -------------------------------

def label_cluster(row):
    if row["Cluster"] == 0:
        return "Top Performer"
    elif row["Cluster"] == 1:
        return "Average Student"
    else:
        return "Struggling Student"

data["Category"] = data.apply(label_cluster, axis=1)

print("\nSample Data with Categories:\n")
print(data.head())

# -------------------------------
# Step 7: Visualization
# -------------------------------

plt.scatter(data["PreviousScore"], data["StudyHours"], c=data["Cluster"])
plt.xlabel("Previous Score")
plt.ylabel("Study Hours")
plt.title("Student Clusters")
plt.show()