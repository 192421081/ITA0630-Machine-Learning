from sklearn.tree import DecisionTreeClassifier
from sklearn import datasets

iris = datasets.load_iris()
model = DecisionTreeClassifier()
model.fit(iris.data, iris.target)

print("Prediction:", model.predict([iris.data[0]]))
