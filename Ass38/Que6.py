# Plot a histogram of StudyHours.
# Explain what the distribution tells you.

import pandas as pd
import matplotlib.pylab as plt

dataSet="student_performance_ml.csv"
dataFrame=pd.read_csv(dataSet)

plt.figure()
plt.hist(dataFrame["StudyHours"],bins=10)
plt.xlabel("StudyHours")
plt.ylabel("Number of students")
plt.title("Distribution of StudyHours:")
plt.show()