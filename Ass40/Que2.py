# 2. Remove the column SleepHours from the dataset. Train the model again.
# Compare new accuracy with previous accuracy.
# Does removing this feature affect performance?

import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

dataSet="student_performance_ml.csv"
dataFrame=pd.read_csv(dataSet)

data_new=dataFrame.drop("SleepHours", axis=1)

X=data_new.drop("FinalResult",axis=1)
y=data_new["FinalResult"]

X_train,X_test,y_train,y_test=train_test_split(
    X,
    y,
    random_state=42,
    test_size=0.2
)

model=DecisionTreeClassifier(max_depth=3,random_state=42)
model.fit(X_train,y_train)

y_pred=model.predict(X_test)

acc=accuracy_score(y_test,y_pred)

print("New Accuracy (without SleepHours): {:.2f}%".format(acc * 100))