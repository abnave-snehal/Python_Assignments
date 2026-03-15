import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.metrics.pairwise import euclidean_distances

# Two points
point1 = [25, 20000]
point2 = [35, 80000]

data = np.array([point1, point2])

print("Original Points:")
print(data)

# Euclidean distance before scaling
dist_before = euclidean_distances([point1],[point2])
print("\nEuclidean Distance before scaling:",dist_before[0][0])

# Apply feature scaling
scaler = StandardScaler()
scaled_data = scaler.fit_transform(data)

print("\nScaled Data:")
print(scaled_data)

# Euclidean distance after scaling
dist_after = euclidean_distances([scaled_data[0]],[scaled_data[1]])
print("\nEuclidean Distance after scaling:",dist_after[0][0])