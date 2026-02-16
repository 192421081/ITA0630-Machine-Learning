from sklearn.naive_bayes import GaussianNB
from sklearn.datasets import load_iris
from sklearn.metrics import accuracy_score

data = load_iris()
model = GaussianNB()
model.fit(data.data, data.target)

pred = model.predict(data.data)
print("Accuracy:", accuracy_score(data.target, pred))
