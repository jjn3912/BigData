import seaborn as sns
import pandas as pd

titanic = sns.load_dataset('titanic')

age_survived = titanic.groupby(pd.cut(titanic['age'],list(range(0, 81, 10))))['survived'].sum()
print(age_survived)


