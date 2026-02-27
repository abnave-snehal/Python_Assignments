# Train model with: max_depth = None Calculate: 1)Training accuracy 2)Testing accuracy
# If training accuracy is 100% but testing accuracy is lower, explain why this happens.

import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Load dataset
dataSet = "student_performance_ml.csv"
dataFrame = pd.read_csv(dataSet)

# Prepare features and target
X = dataFrame.drop("FinalResult", axis=1)
y = dataFrame["FinalResult"]

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train model with max_depth=None (fully grown tree)
model = DecisionTreeClassifier(max_depth=None, random_state=42)
model.fit(X_train, y_train)

# Training predictions
y_train_pred = model.predict(X_train)

# Testing predictions
y_test_pred = model.predict(X_test)

# Calculate accuracy
train_accuracy = accuracy_score(y_train, y_train_pred)
test_accuracy = accuracy_score(y_test, y_test_pred)

print("Training Accuracy:", train_accuracy * 100, "%")
print("Testing Accuracy:", test_accuracy * 100, "%")