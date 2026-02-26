# Use value_counts() to analyze the distribution of FinalResult.
# Calculate the percentage of Pass and Fail students.
# Is the dataset balanced? Justify your answer.

import pandas as pd

dataSet="student_performance_ml.csv"
dataFrame=pd.read_csv(dataSet)

count=dataFrame["FinalResult"].value_counts()
print("Value count : ",count)

# Total students
total=len(dataFrame)


pass_cal=(count[1] / total) * 100
fail_cal=(count[0] / total) * 100

print("Pass Percentage : {:.2f}%".format(pass_cal))
print("Fail Percentage : {:.2f}%".format(fail_cal))

if abs(pass_cal - fail_cal) < 10:
    print("The dataset is balanced.")
else:
    print("The dataset is not balanced.")