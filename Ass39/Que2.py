# Use the trained model to predict results for X_test.
# Display predicted values along with actual values.

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
import pandas as pd

dataSet="student_performance_ml.csv"
dataFrame=pd.read_csv(dataSet)

X=dataFrame.drop("FinalResult",axis=1)
y=dataFrame["FinalResult"]

X_train,X_test,y_train,y_test=train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

model=DecisionTreeClassifier()

train_result=model.fit(X_train,y_train)

test_result=train_result.predict(X_test)

results=pd.DataFrame({
    "Actual":y_test.values,
    "Predicted":test_result
})

print("\nComparisen:")
print(results)