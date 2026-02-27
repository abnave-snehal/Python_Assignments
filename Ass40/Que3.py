# Train the model using only: 1)StudyHours 2)Attendance
# Compare the accuracy with the full-feature model.Is the model still performing well?

import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

dataSet = "student_performance_ml.csv"
dataFrame = pd.read_csv(dataSet)

# Use only StudyHours and Attendance
X = dataFrame[["StudyHours", "Attendance"]]
y = dataFrame["FinalResult"]

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Train model
model = DecisionTreeClassifier(max_depth=3, random_state=42)
model.fit(X_train, y_train)

# Predict
y_pred = model.predict(X_test)

# Accuracy
accuracy = accuracy_score(y_test, y_pred)

print("Accuracy using only StudyHours & Attendance: {:.2f}%".format(accuracy * 100))