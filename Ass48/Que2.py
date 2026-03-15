import numpy as np

# Dataset
data = np.array([6,7,8,9,10,11,12])

# Calculate variance
variance = np.var(data)

# Calculate standard deviation
std_dev = np.std(data)

# Display results
print("Dataset :",data)
print("Variance :",variance)
print("Standard Deviation :",std_dev)