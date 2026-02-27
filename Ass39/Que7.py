# 7. Use the trained model to predict result for a student with:
# StudyHours = 6, Attendance = 85, PreviousScore = 66, AssignmentsCompleted = 7
# SleepHours = 7 Will the student Pass or Fail?

import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split

dataSet="student_performance_ml.csv"
dataFrame=pd.read_csv(dataSet)

X=dataFrame.drop("FinalResult",axis=1)
y=dataFrame["FinalResult"]

X_train,X_test,y_train,y_test=train_test_split(
    X,
    y,
    random_state=42,
    test_size=0.2
)

model3=DecisionTreeClassifier(max_depth=None,random_state=42)
model3.fit(X_train,y_train)

students=pd.DataFrame([{
    "StudyHours": 6,
    "Attendance": 85,
    "PreviousScore": 66, 
    "AssignmentsCompleted": 7,
    "SleepHours": 7
}])

prediction=model3.predict(students)

print("Prediction Result : ",prediction[0])