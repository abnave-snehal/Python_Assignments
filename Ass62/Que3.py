# Input Matrix
matrix = [
    [6, 4],
    [8, 6]
]

# Flatten
flatten_output = []
for row in matrix:
    for val in row:
        flatten_output.append(val)

print("Flatten Output:", flatten_output)

# Fully Connected Layer (example weights & bias)
weights = [0.5, 0.2, 0.1, 0.7]
bias = 1

# Manual Calculation
output = 0
for i in range(len(flatten_output)):
    output += flatten_output[i] * weights[i]

output += bias

print("Final Output:", output)