import seaborn as sns
import pandas as pd

titanic = sns.load_dataset('titanic')

survived_human = titanic[titanic["survived"] == 1]["survived"].count()
dead_human = titanic[titanic["survived"] == 0]["survived"].count()
male_survived =  titanic[(titanic["survived"] == 1 )&(titanic["sex"] == 'male')]["survived"].count()
female_survived =  titanic[(titanic["survived"] == 1 )&(titanic["sex"] == 'female')]["survived"].count()
male_count =  titanic[titanic["sex"] == 'male']["sex"].count()
female_count =  titanic[titanic["sex"] == 'female']["sex"].count()
print(f"생존자 수 :{survived_human}명")
print(f"사망자 수 :{dead_human}명")
print(male_count,female_count)
print(male_survived/male_count,female_survived/female_count)

