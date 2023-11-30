import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
titanic = sns.load_dataset('titanic')

survived_ages = titanic[titanic['survived'] == 1]['age'].dropna()
dead_ages = titanic[titanic['survived'] == 0]['age'].dropna()

plt.hist(survived_ages, 20, label='survived',alpha = 0.5)
plt.hist(dead_ages, 20, label = 'dead',alpha = 0.5)
plt.xlabel('age')
plt.ylabel('Count')
plt.legend()
plt.show()
