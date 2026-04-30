# ==========================================================
# Customer Churn Prediction using ANN (TensorFlow/Keras)
# ==========================================================

import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, classification_report
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

# ----------------------------------------------------------
# Features:
# [Age, Monthly Charges, Tenure, Complaints, Support Calls]
# ----------------------------------------------------------

X = np.array([
    [25, 500, 12, 1, 2],
    [45, 700, 24, 0, 1],
    [30, 1200, 6, 1, 3],
    [50, 1500, 5, 1, 0],
    [28, 600, 18, 1, 1],
    [38, 900, 30, 0, 0],
    [42, 1400, 4, 1, 2],
    [52, 1600, 3, 0, 2],
    [27, 550, 20, 0, 1],
    [35, 1300, 8, 1, 4]
])

# Output:
# 0 = Customer will stay
# 1 = Customer will leave

y = np.array([0, 0, 1, 1, 0, 0, 1, 1, 0, 1])

# ----------------------------------------------------------
# Split data
# ----------------------------------------------------------
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# ----------------------------------------------------------
# Feature Scaling
# ----------------------------------------------------------
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# ----------------------------------------------------------
# Build ANN Model
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
# Train Model
# ----------------------------------------------------------
model.fit(X_train, y_train, epochs=100, verbose=0)

# ----------------------------------------------------------
# Evaluate Model
# ----------------------------------------------------------
loss, accuracy = model.evaluate(X_test, y_test, verbose=0)

print("Test Accuracy =", round(accuracy * 100, 2), "%")

# ----------------------------------------------------------
# Test New Customer
# ----------------------------------------------------------
new_customer = np.array([[40, 1450, 5, 0, 3]])

new_customer = scaler.transform(new_customer)

prediction = model.predict(new_customer, verbose=0)

if prediction[0][0] > 0.5:
    print("Prediction: Customer will leave")
else:
    print("Prediction: Customer will stay")