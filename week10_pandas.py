import numpy as np
import matplotlib.pyplot as plt
#linalg == linear algebra
np.random.seed()
a = np.random.uniform(size = 10000)# 균등분포
b = np.random.normal(0, 1, 10000) #정규분포
print(a)
print(b)
plt.hist(b)
plt.show()
