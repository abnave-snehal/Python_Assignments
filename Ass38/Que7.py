# 7. Create a scatter plot of:
# StudyHours vs PreviousScore. Use different color for pass and fail students.

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

dataSet="student_performance_ml.csv"
dataFrame=pd.read_csv(dataSet)

sns.scatterplot(
    data=dataFrame,
    x="StudyHours",
    y="PreviousScore",
    hue="FinalResult",
    palette={0:"red",1:"green"}
    )

plt.title("StudyHours Vs PreviousScores")
plt.show()