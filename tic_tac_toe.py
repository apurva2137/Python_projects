import csv
from collections import defaultdict
import numpy as np

class NaiveBayes:
    def __init__(self):
        self.class_probabilities = None
        self.feature_probabilities = None

    def fit(self, X, y):
        n_samples, n_features = X.shape
        self.classes = np.unique(y)
        n_classes = len(self.classes)

    
        self.class_probabilities = np.zeros(n_classes)
        for i, c in enumerate(self.classes):
            self.class_probabilities[i] = np.sum(y == c) / float(n_samples)

        # Calculate feature probabilities
        self.feature_probabilities = {}
        for c in self.classes:
            c_mask = y == c
            self.feature_probabilities[c] = []
            for i in range(n_features):
                feature_values = X[c_mask][:, i]
                unique_values, counts = np.unique(feature_values, return_counts=True)
                prob = {}
                for value, count in zip(unique_values, counts):
                    prob[value] = count / float(np.sum(c_mask))
                self.feature_probabilities[c].append(prob)

    def _calculate_class_probability(self, x, c):
        probability = np.log(self.class_probabilities[c])
        for i, feature_value in enumerate(x):
            if feature_value in self.feature_probabilities[c][i]:
                probability += np.log(self.feature_probabilities[c][i][feature_value])
            else:
                probability += np.log(1e-6)  
        return probability

    def predict(self, X):
        predictions = []
        for x in X:
            max_probability = -np.inf
            predicted_class = None
            for i, c in enumerate(self.classes):
                class_probability = self._calculate_class_probability(x, i)
                if class_probability > max_probability:
                    max_probability = class_probability
                    predicted_class = c
            predictions.append(predicted_class)
        return predictions

def load_dataset(filename):
    X = []
    y = []
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        headers = next(reader)
        for row in reader:
            X.append(row[:-1])  
            y.append(row[-1])   
    return np.array(X), np.array(y)

def preprocess_data(X):
    label_encoders = []
    for i in range(X.shape[1]):
        unique_values = np.unique(X[:, i])
        label_encoder = {value: j for j, value in enumerate(unique_values)}
        label_encoders.append(label_encoder)
        X[:, i] = [label_encoder[value] for value in X[:, i]]
    return X, label_encoders

def main():
    filename = 'play_tennis.csv'
    X, y = load_dataset(filename)
    X, _ = preprocess_data(X)
    model = NaiveBayes()
    model.fit(X, y)
    X_test = np.array([[1, 2, 0, 1], [0, 1, 1, 0]])
    predictions = model.predict(X_test)
    print("Predictions:", predictions)

if __name__ == "__main__":
    main()
