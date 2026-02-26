# Using pandas functions, calculate and display: 1)Average StudyHours
# 2) Average Attendance 3) Maximum PreviousScore 4) Minimum SleepHours

import pandas as pd

dataSet="student_performance_ml.csv"
dataFrame=pd.read_csv(dataSet)

# Average StudyHours
avgsHours=dataFrame["StudyHours"].mean()
print("Average Study Hours : ",avgsHours)

# Average Attendance
avgAtt=dataFrame["Attendance"].mean()
print("Average Attendance : ",avgAtt)

# Maximum Previous Score
maxpreScore=dataFrame["PreviousScore"].max()
print("Maximum Previous Score : ",maxpreScore)

# Minimum Sleep Hours
minsleepHour=dataFrame["SleepHours"].min()
print("Minimum Sleep Hours : ",minsleepHour)