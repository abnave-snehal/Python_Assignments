# 3. Calculate model accuracy using accuracy_score.
# Display the result in percentage format.

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
import pandas as pd
from sklearn.metrics import (
    accuracy_score
)

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

Accuracy=accuracy_score(y_test,test_result)

print("Accuracy of Model is : {:.2f}%".format(Accuracy * 100))