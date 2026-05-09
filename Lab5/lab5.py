import numpy as np
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

class Node:
    def __init__(self, index, t, true_branch, false_branch):
        self.index = index
        self.t = t
        self.true_branch = true_branch
        self.false_branch = false_branch


class Leaf:
    def __init__(self, data, labels):
        self.data = data
        self.labels = labels
        self.prediction = self.predict()

    def predict(self):
        classes, counts = np.unique(self.labels, return_counts=True)
        return classes[np.argmax(counts)]

def gini(labels):
    _, counts = np.unique(labels, return_counts=True)
    probabilities = counts / len(labels)
    return 1 - np.sum(probabilities ** 2)

def entropy(labels):
    _, counts = np.unique(labels, return_counts=True)
    probabilities = counts / len(labels)
    return -np.sum(probabilities * np.log2(probabilities + 1e-10))

def gain(left_labels, right_labels, root_criterion):
    p = float(len(left_labels)) / (len(left_labels) + len(right_labels))
    return root_criterion - p * gini(left_labels) - (1 - p) * gini(right_labels)

def split(data, labels, index, t):
    left_mask = data[:, index] <= t
    right_mask = ~left_mask
    return data[left_mask], data[right_mask], labels[left_mask], labels[right_mask]

def find_best_split(data, labels):
    root_gini = gini(labels)
    best_gain = 0
    best_t = None
    best_index = None

    n_features = data.shape[1]

    for index in range(n_features):
        t_values = np.unique(data[:, index])
        for t in t_values:
            l_data, r_data, l_labels, r_labels = split(data, labels, index, t)

            if len(l_data) == 0 or len(r_data) == 0:
                continue

            current_gain = gain(l_labels, r_labels, root_gini)

            if current_gain > best_gain:
                best_gain, best_t, best_index = current_gain, t, index

    return best_gain, best_t, best_index

def build_tree(data, labels, current_depth=0, max_depth=5, min_samples_leaf=5):
    if current_depth >= max_depth:
        return Leaf(data, labels)

    if len(data) <= min_samples_leaf:
        return Leaf(data, labels)

    quality, t, index = find_best_split(data, labels)

    if quality == 0:
        return Leaf(data, labels)

    true_data, false_data, true_labels, false_labels = split(data, labels, index, t)

    true_branch = build_tree(true_data, true_labels, current_depth + 1, max_depth, min_samples_leaf)
    false_branch = build_tree(false_data, false_labels, current_depth + 1, max_depth, min_samples_leaf)

    return Node(index, t, true_branch, false_branch)

def classify_object(obj, node):
    if isinstance(node, Leaf):
        return node.prediction

    if obj[node.index] <= node.t:
        return classify_object(obj, node.true_branch)
    else:
        return classify_object(obj, node.false_branch)


def predict(data, tree):
    return [classify_object(obj, tree) for obj in data]

def calc_accuracy(y_true, y_pred):
    return np.mean(y_true == y_pred)

X, y = make_classification(n_samples=300, n_features=5, n_informative=3, n_classes=2, random_state=42)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

MAX_DEPTH = 3
MIN_SAMPLES = 5

my_tree = build_tree(X_train, y_train, max_depth=MAX_DEPTH, min_samples_leaf=MIN_SAMPLES)
my_preds = predict(X_test, my_tree)
my_acc = calc_accuracy(y_test, my_preds)

sk_tree = DecisionTreeClassifier(max_depth=MAX_DEPTH, min_samples_leaf=MIN_SAMPLES, random_state=42, criterion='gini')
sk_tree.fit(X_train, y_train)
sk_preds = sk_tree.predict(X_test)
sk_acc = accuracy_score(y_test, sk_preds)

print(f"Accuracy (Custom Tree): {my_acc:.4f}")
print(f"Accuracy (Sklearn Tree): {sk_acc:.4f}")

if abs(my_acc - sk_acc) < 0.05:
    print("\nРезультаты сошлись (небольшая разница допустима из-за нюансов реализации в sklearn)!")