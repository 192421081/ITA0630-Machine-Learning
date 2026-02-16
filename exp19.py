from sklearn.naive_bayes import GaussianNB
import numpy as np

X = np.array([[50000,700],[30000,500],[80000,750]])
y = [1,0,1]

model = GaussianNB()
model.fit(X,y)

print("Loan Status:", model.predict([[60000,720]]))
