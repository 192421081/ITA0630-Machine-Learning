from sklearn.linear_model import LinearRegression
import numpy as np

X = np.array([[1],[2],[3],[4]])
y = [100,200,300,400]

model = LinearRegression()
model.fit(X,y)

print("Future Sales:", model.predict([[6]]))
