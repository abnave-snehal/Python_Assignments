# ==========================================================
# 2. Python program for different activation functions
# ==========================================================

import numpy as np
import matplotlib.pyplot as plt

# Input values from -10 to 10
x=np.linspace(-10,10,200)

# Activation Functions
def sigmoid(x):
    return 1/(1+np.exp(-x))

def relu(x):
    return np.maximum(0,x)

def tanh(x):
    return np.tanh(x)

# Compute outputs
y_sigmoid=sigmoid(x)
y_relu=relu(x)
y_tanh=tanh(x)

# Plotting
plt.figure(figsize=(10,6))

plt.plot(x,y_sigmoid,label="Sigmoid")
plt.plot(x,y_relu,label="ReLU")
plt.plot(x, y_tanh, label="Tanh")

plt.title("Activation Functions")
plt.xlabel("Input")
plt.ylabel("Output")
plt.legend()
plt.grid(True)
plt.show()