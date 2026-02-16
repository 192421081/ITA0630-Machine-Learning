from sklearn.tree import DecisionTreeClassifier
import numpy as np

X = np.array([[4,64],[6,128],[8,256]])
y = [0,1,2]

model = DecisionTreeClassifier()
model.fit(X,y)

print("Category:", model.predict([[6,128]]))
