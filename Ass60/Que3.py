# ==========================================================
# 3. Python program to calculate loss manually
# ==========================================================

import math

# Example values
actual=1
predicted=0.8

# Mean Squared Error (MSE)
mse=(actual - predicted) **2

# Binary Cross Entropy (BCE)
bce=-(actual * math.log(predicted) + (1-actual) * math.log(1-predicted))

# Display results
print("Actual Value     =", actual)
print("Predicted Value  =", predicted)
print("MSE Loss         =", mse)
print("Binary Cross Entropy Loss =", bce)

# Explanation
print("\nLoss Function Usage:")
print("MSE is used for Regression problems.")
print("Binary Cross Entropy is used for Binary Classification problems.")
