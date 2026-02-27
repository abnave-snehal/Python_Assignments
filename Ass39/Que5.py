# Calculate: 1)Training accuracy 2)Testing accuracy
# Compare both and comment whether the model is overfitting or underfitting.

import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import(
    accuracy_score,confusion_matrix,ConfusionMatrixDisplay
)
import matplotlib.pyplot as plt

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

#Training
train_result=model.predict(X_train)

#Testing
test_result=model.predict(X_test)

#Calculate accuracy
train_accuracy=accuracy_score(y_train,train_result)
test_accuracy=accuracy_score(y_test,test_result)

print("Training accuracy: {:.2f}%".format(train_accuracy * 100))
print("Test accuracy: {:.2f}%".format(test_accuracy * 100))