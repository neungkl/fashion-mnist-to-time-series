import dtwco
from sklearn.neighbors import KNeighborsClassifier

class KnnDtw:
    def __init__(self, n_neighbors=5, dtw_constraint=None):
        self.clf = self.construct_knn_classifier(n_neighbors=n_neighbors, dtw_constraint=dtw_constraint)
    
    def construct_knn_classifier(self, n_neighbors=5, dtw_constraint=None):
        # Constructs the kNN Regressor under a DTW metric
        dtw_metric = lambda x, y: dtwco.dtw(x, y, metric='euclidean', constraint=dtw_constraint, dist_only=True)
        clf = KNeighborsClassifier(n_neighbors=5, metric=dtw_metric, n_jobs=1)
        return clf
    
    def fit(self, X, y):
        # Fit the model using X as training data and y as target values
        self.clf.fit(X, y)

    def predict(self, X):
        # Predict the class labels for the provided data
        return self.clf.predict(X)