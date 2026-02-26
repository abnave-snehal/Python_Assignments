# 2. Write a program to: 1) Display total number of students in the dataset
# 2) Count how many students Passed (FinalResult = 1)
# 3) Count how many students Failed (FinalResult = 0)

import pandas as pd

border="_"*100

dataSet="student_performance_ml.csv"
dataFrame=pd.read_csv(dataSet)


datasetLenth=len(dataFrame)
print(border)
print("Total number of student in the dataset are:",datasetLenth)
print(border)


print(border)
print("Count of passed student : ",(dataFrame["FinalResult"]==1).sum())
print(border)

print(border)
print("Count of failed student : ",(dataFrame["FinalResult"] == 0).sum())
print(border)