# Create a new column: PerformanceIndex = (StudyHours * 2) + Attendance
# Train the model including this new feature. Does accuracy improve?

import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Load dataset
dataSet = "student_performance_ml.csv"
dataFrame = pd.read_csv(dataSet)

# -----------------------------
# Model WITHOUT PerformanceIndex
# -----------------------------

X = dataFrame.drop("FinalResult", axis=1)
y = dataFrame["FinalResult"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model1 = DecisionTreeClassifier(max_depth=3, random_state=42)
model1.fit(X_train, y_train)

y_pred1 = model1.predict(X_test)
acc_without = accuracy_score(y_test, y_pred1)

print("Accuracy WITHOUT PerformanceIndex:", acc_without * 100)


# -----------------------------
# Add New Feature
# -----------------------------

dataFrame["PerformanceIndex"] = (
    dataFrame["StudyHours"] * 2
) + dataFrame["Attendance"]

# Prepare new feature set
X_new = dataFrame.drop("FinalResult", axis=1)
y_new = dataFrame["FinalResult"]

X_train2, X_test2, y_train2, y_test2 = train_test_split(
    X_new, y_new, test_size=0.2, random_state=42
)

model2 = DecisionTreeClassifier(max_depth=3, random_state=42)
model2.fit(X_train2, y_train2)

y_pred2 = model2.predict(X_test2)
acc_with = accuracy_score(y_test2, y_pred2)

print("Accuracy WITH PerformanceIndex:", acc_with * 100)