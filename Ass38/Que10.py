# Plot SleepHours against FinalResult.
# Does sleeping more guarantee success? Explain.

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

dataSet="student_performance_ml.csv"
dataFrame=pd.read_csv(dataSet)

sns.boxplot(data=dataFrame,y="SleepHours",x="FinalResult")

plt.title("SleepHours Vs FinalResult")
plt.xlabel("FinalResult")
plt.ylabel("SleepHours")
plt.show()