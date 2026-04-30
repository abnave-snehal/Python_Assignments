# ==========================================================
# Neural Network Model to Predict Loan Approval
# ==========================================================

import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

# ----------------------------------------------------------
# Features:
# [Income, Credit Score, Loan Amount, Existing EMI, Employment]
# Employment: 0 = Not Stable, 1 = Stable
# ----------------------------------------------------------

X = np.array([
    [25000, 600, 20000, 1000, 0],
    [40000, 750, 30000,  800, 1],
    [60000, 780, 50000, 1200, 1],
    [20000, 550, 15000, 1500, 0],
    [50000, 690, 25000, 1000, 1],
    [35000, 650, 18000,  900, 1],
    [18000, 500, 10000, 1200, 0],
    [70000, 800, 60000, 1500, 1],
    [30000, 580, 20000, 1400, 0],
    [45000, 720, 28000, 1000, 1]
])

# Output:
# 0 = Loan Rejected
# 1 = Loan Approved

y = np.array([0,1,1,0,1,1,0,1,0,1])

# ----------------------------------------------------------
# Split Data
# ----------------------------------------------------------
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# ----------------------------------------------------------
# Scaling
# ----------------------------------------------------------
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# ----------------------------------------------------------
# Build ANN
# ----------------------------------------------------------
model = Sequential()
model.add(Dense(8, activation='relu', input_shape=(5,)))
model.add(Dense(4, activation='relu'))
model.add(Dense(1, activation='sigmoid'))

model.compile(
    optimizer='adam',
    loss='binary_crossentropy',
    metrics=['accuracy']
)

# ----------------------------------------------------------
# Train
# ----------------------------------------------------------
model.fit(X_train, y_train, epochs=100, verbose=0)

# ----------------------------------------------------------
# Evaluate
# ----------------------------------------------------------
loss, accuracy = model.evaluate(X_test, y_test, verbose=0)
print("Test Accuracy =", round(accuracy*100,2), "%")

# ----------------------------------------------------------
# Test Input from Question
# ----------------------------------------------------------
new_applicant = np.array([[55000, 720, 40000, 1000, 1]])

new_scaled = scaler.transform(new_applicant)

prediction = model.predict(new_scaled, verbose=0)

if prediction[0][0] > 0.5:
    print("Prediction: Loan Approved")
else:
    print("Prediction: Loan Rejected")