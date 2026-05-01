feature_map = [
    [3, 3, 3],
    [0, 0, 0],
    [-3, -3, -3]
]

# ReLU Function
relu_output = []
for row in feature_map:
    relu_row = [max(0, val) for val in row]
    relu_output.append(relu_row)

print("ReLU Output:")
for row in relu_output:
    print(row)

# Max Pooling (2x2)
pooled_output = []

for i in range(0, len(relu_output) - 1, 2):
    row = []
    for j in range(0, len(relu_output[0]) - 1, 2):
        block = [
            relu_output[i][j],
            relu_output[i][j+1],
            relu_output[i+1][j],
            relu_output[i+1][j+1]
        ]
        row.append(max(block))
    pooled_output.append(row)

print("\nMax Pooling Output:")
for row in pooled_output:
    print(row)