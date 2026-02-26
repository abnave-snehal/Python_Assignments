# Draw a boxplot for Attendance.
# Identify if any outliers are present.

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

dataSet="student_performance_ml.csv"
dataFrame=pd.read_csv(dataSet)

sns.boxplot(y=dataFrame["Attendance"])

plt.title("Box plot of Attendance")
plt.ylabel("Attendance")
plt.show()
