from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import OneHotEncoder
import numpy as np


def train_and_evaluate_model(data):
    data_np = np.array(list(data.values()))

    encoder = OneHotEncoder(sparse=False)
    one_hot_encoded_data = encoder.fit_transform(data_np)

    y = list(data.keys())

    label_dict = {'normal_skin': 0, 'oily_skin': 1,
                  'dry_skin': 2, 'combination_skin': 3, 'sensitive_skin': 4}
    y_numeric = [label_dict[label] for label in y]

    X_train, X_test, y_train, y_test = train_test_split(
        one_hot_encoded_data, y_numeric, test_size=0.2, random_state=42)

    clf = DecisionTreeClassifier()
    clf.fit(X_train, y_train)

    accuracy = accuracy_score(y_test, clf.predict(X_test))
    return accuracy


data = {
    "normal_skin": [0, -1, 0, 1, 0],
    "oily_skin": [1, 1, 1, 0, 1],
    "dry_skin": [-1, -1, -1, -1, -1],
    "combination_skin": [0.5, 0, 0.5, 0, 0],
    "sensitive_skin": [-0.5, 0, -0.5, 1, 1]
}

print(train_and_evaluate_model(data))
