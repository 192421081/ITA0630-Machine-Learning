from sklearn.naive_bayes import GaussianNB
from sklearn.datasets import load_iris

data = load_iris()
model = GaussianNB()
model.fit(data.data,data.target)

print("Accuracy:", model.score(data.data,data.target))
