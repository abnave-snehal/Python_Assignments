# ==========================================================
# 1. Python program to simulate a single artificial neuron
# ==========================================================

import math

# Input values
x1 = 2
x2 = 3

w1 = 0.4
w2 = 0.6

bias = 0.5

# Step 1: Calculate weighted sum
weighted_sum=(x1*w1) + (x2*w2) + bias

# Step 2: Apply sigmoid activation function
output=1/(1+math.exp(-weighted_sum))

# Step 3: Display final output
print("Weighted Sum : ",weighted_sum)
print("Neuron Output : ",output)

# Step 4: Explain result
if output>0.5:
    print("Output is close to 1")
else:
    print("Output is close to 0")