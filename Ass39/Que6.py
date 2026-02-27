# Train three Decision Tree models with: 1)max_depth = 1  2)max_depth = 3
# 3)max_depth = None  Compare their testing accuracies and write your observations.

import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import(
    accuracy_score,confusion_matrix,ConfusionMatrixDisplay
)
from sklearn.model_selection import train_test_split


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

# Model 1: max_depth = 1
model1=DecisionTreeClassifier(max_depth=1)
model1.fit(X_train,y_train)
pred1=model1.predict(X_test)
acc1=accuracy_score(y_test,pred1)

# Model 2: max_depth=3
model2=DecisionTreeClassifier(max_depth=3)
model2.fit(X_train,y_train)
pred2=model2.predict(X_test)
acc2=accuracy_score(y_test,pred2)


# Model 3: max_depth=None
model3=DecisionTreeClassifier(max_depth=None)
model3.fit(X_train,y_train)
pred3=model3.predict(X_test)
acc3=accuracy_score(y_test,pred3)

print("Accuracy (max_depth=1): {:.2f}%".format(acc1 * 100))
print("Accuracy (max_depth=3): {:.2f}%".format(acc2 * 100))
print("Accuracy (max_depth=None): {:.2f}%".format(acc3 * 100))
