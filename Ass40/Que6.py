# Identify students where: y_test != y_pred Display those rows.
#  How many students were misclassified? What common pattern do you observe?

import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import(
    accuracy_score
)

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

y_pred=model.predict(X_test)

# Create comparison DataFrame
result=X_test.copy()
result["Actual"]=y_test.values
result["Predicted"]=y_pred

# Identify misclassified students
misclassified = result[result["Actual"] != result["Predicted"]]

print("Misclassified Students:",misclassified)

print("\nNumber of Misclassified Students:", len(misclassified))



