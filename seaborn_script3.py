import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns

df = pd.read_csv("survey.csv")
# print(df)
# My code begins
sns.barplot(
  data=df,
  x='Age Range',
  y='Response',
  hue="Gender"
)
plt.show()
