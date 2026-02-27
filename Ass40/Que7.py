# Train model using: random_state = 0, random_state = 10, random_state = 42
# Compare testing accuracy.  Does the result change?

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

# Try different random_state values
states = [0, 10, 42]

for state in states:
    
    # Split dataset using different random_state
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=state
    )
    
    # Train model
    model = DecisionTreeClassifier(max_depth=3, random_state=state)
    model.fit(X_train, y_train)
    
    # Predict
    y_pred = model.predict(X_test)
    
    # Calculate accuracy
    acc = accuracy_score(y_test, y_pred)
    
    print(f"Random State = {state} → Testing Accuracy = {acc * 100:.2f}%")