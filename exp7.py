from sklearn.linear_model import LogisticRegression
from sklearn.datasets import load_iris

data = load_iris()
model = LogisticRegression(max_iter=200)
model.fit(data.data, data.target)

print("Prediction:", model.predict([data.data[0]]))
