from sklearn.ensemble import RandomForestClassifier
import numpy as np

X = np.array([[25,50000],[40,80000],[22,20000]])
y = [1,1,0]

model = RandomForestClassifier()
model.fit(X,y)

print("Prediction:", model.predict([[30,60000]]))
