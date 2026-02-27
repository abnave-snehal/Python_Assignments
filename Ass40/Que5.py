# 5. Without using accuracy_score, manually calculate accuracy:
# Verify whether it matches sklearn accuracy.

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

correct=0
total=len(y_pred)

for actual,predicted in zip(y_test,y_pred):
    if actual==predicted:
        correct+=1

manual_acc= correct / total

print("Manual Accuracy",manual_acc * 100, "%")

sklen_acc=accuracy_score(y_test,y_pred)

print("Sklearn Accuracy:", sklen_acc * 100, "%")