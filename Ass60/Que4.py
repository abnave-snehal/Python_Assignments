# ==========================================================
# 4. Python program to show weight update in ANN
# ==========================================================

# ==========================================================
# 4. Python program to show weight update in ANN
# ==========================================================

# Input values
x = 2
weight = 0.5
bias = 0.1
target = 1
learning_rate = 0.1

# Step 1: Prediction
prediction = (x * weight) + bias

# Step 2: Error
error = target - prediction

# Step 3: Update weight using gradient descent
new_weight = weight + learning_rate * error * x

# Display results
print("Old Weight =", weight)
print("Prediction =", prediction)
print("Error      =", error)
print("Updated Weight =", new_weight)