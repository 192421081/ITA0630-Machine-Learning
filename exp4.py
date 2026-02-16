from sklearn.neural_network import MLPClassifier
from sklearn import datasets

iris = datasets.load_iris()
model = MLPClassifier(max_iter=1000)
model.fit(iris.data, iris.target)

print("Accuracy:", model.score(iris.data, iris.target))
