from sklearn.linear_model import LinearRegression
import numpy as np

X = np.array([[2],[3],[4]])
y = [200000,300000,400000]

model = LinearRegression()
model.fit(X,y)

print("Price:", model.predict([[5]]))
