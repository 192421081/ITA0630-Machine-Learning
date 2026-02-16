from sklearn.linear_model import LinearRegression
import numpy as np

X = np.array([[1000],[2000],[3000]])
y = [20000,30000,40000]

model = LinearRegression()
model.fit(X,y)

print("Price:", model.predict([[2500]]))
