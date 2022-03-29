import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns

df = pd.read_csv("survey.csv")

# sns.barplot(data=df, x="Gender", y="Patient ID", hue="Age Range")

sns.barplot(data=df, x="Age Range", y="Patient ID", hue="Gender")

plt.show()