from sklearn.neighbors import KNeighborsClassifier
from sklearn.datasets import load_iris

data = load_iris()
model = KNeighborsClassifier()
model.fit(data.data,data.target)

print("Accuracy:", model.score(data.data,data.target))
