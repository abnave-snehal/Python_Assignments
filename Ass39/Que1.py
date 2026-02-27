# Import DecisionTreeClassifier from sklearn.
# Create a model object and train it using fit().

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

model.fit(X_train,y_train)

print("Model train successfully!")