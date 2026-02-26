# Create a plot showing relationship between AssignmentsCompleted and FinalResult.
# Explain your observation.

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

dataSet="student_performance_ml.csv"
dataFrame=pd.read_csv(dataSet)

sns.boxplot(x="FinalResult",y="AssignmentsCompleted",data=dataFrame)

plt.title("AssignmentsCompleted Vs FinalResult")
plt.xlabel("FinalResult")
plt.ylabel("AssignmentsCompleted")
plt.show()
