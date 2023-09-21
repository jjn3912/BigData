import matplotlib.pyplot as plt
import pandas as pd
from sklearn.linear_model import LinearRegression

life_satisfaction = pd.read_csv("https://github.com/ageron/data/raw/main/lifesat/lifesat.csv")
X = life_satisfaction[["GDP per capita (USD)"]].values #return 2d array
y = life_satisfaction[["Life satisfaction"]].values #return 2d array

# print(life_satisfaction.tial(5))
# print(life_satisfaction.shape)
# print(life_satisfaction.describe())
print(X)
print(y)

#draw scatter diagram
life_satisfaction.plot(kind='scatter' , grid=True , x="GDP per capita (USD)" , y="Life satisfaction")
plt.axis([23500,62500, 4 ,9])
plt.show()

model = LinearRegression

model.fit(X,y)

#predict new GDP per capita(South Korea 2020)

X_new = [[31700]]
print(life_satisfaction)
print(model.predict(X_new))