# Create a new DataFrame with details of 5 new students.
# Use the trained model to predict their results. Display predictions clearly.

import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split

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

# Train model
model = DecisionTreeClassifier(max_depth=3, random_state=42)
model.fit(X_train, y_train)

# Create new DataFrame with 5 students
new_students = pd.DataFrame([
    {"StudyHours": 8, "Attendance": 90, "PreviousScore": 75, "AssignmentsCompleted": 9, "SleepHours": 7},
    {"StudyHours": 3, "Attendance": 60, "PreviousScore": 45, "AssignmentsCompleted": 4, "SleepHours": 6},
    {"StudyHours": 6, "Attendance": 80, "PreviousScore": 65, "AssignmentsCompleted": 7, "SleepHours": 8},
    {"StudyHours": 2, "Attendance": 50, "PreviousScore": 40, "AssignmentsCompleted": 3, "SleepHours": 5},
    {"StudyHours": 7, "Attendance": 88, "PreviousScore": 70, "AssignmentsCompleted": 8, "SleepHours": 7}
])


# Predict results
predictions = model.predict(new_students)

# Add predictions column
new_students["PredictedResult"] = predictions

# Display clearly
print("\nPredictions for 5 New Students:")
print(new_students)