from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB

data = load_iris()

models = {
"Logistic":LogisticRegression(max_iter=200),
"KNN":KNeighborsClassifier(),
"NaiveBayes":GaussianNB()
}

for name,model in models.items():
    model.fit(data.data,data.target)
    print(name,"Accuracy:",model.score(data.data,data.target))
