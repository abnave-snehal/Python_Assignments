import numpy as np
from sklearn.preprocessing import StandardScaler

# Dataset
data = np.array([
    [25,20000],
    [30,40000],
    [35,80000]
])

print("Original Dataset:")
print(data)

# Create scaler object
scaler = StandardScaler()

# Perform feature scaling
scaled_data = scaler.fit_transform(data)

print("\nScaled Dataset:")
print(scaled_data)