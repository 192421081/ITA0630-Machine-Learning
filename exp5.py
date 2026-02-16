from sklearn.neighbors import KNeighborsClassifier
from sklearn.datasets import load_iris

data = load_iris()
model = KNeighborsClassifier(n_neighbors=3)
model.fit(data.data, data.target)

print("Prediction:", model.predict([data.data[0]]))
