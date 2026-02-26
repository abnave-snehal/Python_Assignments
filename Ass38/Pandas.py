# 1. Write a Python program to load the file student_performance_m1.csv using pandas. 
# Display: 1)First 5 records 2)Last 5 records 3)Total number of rows and columns
# 4)List of column names 5)Data types of each column

import pandas as pd

border="_"*100

datasetPath="student_performance_ml.csv"
dataFrame=pd.read_csv(datasetPath)

print(border)
print("First 5 Records are.")
print(border)

print(dataFrame.head())  # First 5 records

print(border)
print("Last 5 Records are.")
print(border)

print(dataFrame.tail())  # Last 5 records

print(border)
print("Total number of Rows & Columns:")
print(border)

print("Rows : ",dataFrame.shape[0])
print("Colums :",dataFrame.shape[1])

print(border)
print("List of column name : ",list(dataFrame.columns))
print(border)

print(border)
print("Data type of each Colums:")
print(border)

print(dataFrame.dtypes)
