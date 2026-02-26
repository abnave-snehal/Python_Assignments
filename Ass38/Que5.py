# Based on the dataset values, analyze whether:
# 1) Higher StudyHours increase the chance of passing.
# 2) Higher Attendance improves FinalResult.
# 3) Write your observations in 4–5 lines.

import pandas as pd

dataSet="student_performance_ml.csv"
dataFrame=pd.read_csv(dataSet)

avg=dataFrame.groupby("FinalResult")[["StudyHours","Attendance"]].mean()
print("The Analysis Report is : ")
print(avg)
