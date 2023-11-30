import seaborn as sns
import pandas as pd

titanic = sns.load_dataset('titanic')

pclass_survived= titanic.groupby('pclass')['survived'].sum()
print(pclass_survived)


