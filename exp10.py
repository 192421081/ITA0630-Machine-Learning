from sklearn.mixture import GaussianMixture
import numpy as np

X = np.array([[1],[2],[10],[12]])
model = GaussianMixture(n_components=2)
model.fit(X)

print("Cluster:", model.predict(X))
