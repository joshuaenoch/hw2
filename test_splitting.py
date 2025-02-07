# 1. Write a function to calculate impurity (e.g., Shannon entropy or Gini index).
# 2. Implement a recursive function to split data based on impurity reduction and grow the tree.
# 3. Set stopping conditions to prevent infinite recursion (e.g., max depth, min samples per split, pure nodes).

import pandas as pd
from collections import Counter


class Node:
    def __init__(self, feature=None, threshold=None, left=None, right=None, value=None):
        self.feature = feature
        self.threshold = threshold
        self.left = left
        self.right = right
        self.value = value

    def dealWithNonBinary(
        self,
    ):
        pass


class DecisionTree:
    # we might need hyperparamters based on the rubric, like max-depth
    def __init__(self, data, max_depth=None, min_samples_split=None):
        self.root = None
        self.max_depth = max_depth
        self.min_samples_split = min_samples_split
        self.data = data

    def fit(self, X, y):
        self.root = self.tree_builder(X, y, depth=0)

    # tree builder makes calls to our split() method
    # this method will use recursion to build our tree
    def tree_builder(self, X, y, depth=0):
        node_options = self.data.columns
        print(node_options)
        print("ok")
        self.root = self.split(self.root, node_options, 0, X, y)

    def gini(self, n, total):
        return (n**2) / (total**2)

    # anthony is going to finish this but its complete  rn
    def gini_all(self, node_options):
        ginivalues = []
        for n in range(len(self.data[0])):
            counter = Counter(self.data[:, n])
            ans = 1
            total = counter.total()
            for x in counter.values():
                ans -= self.gini(x, total)
            ginivalues.append(ans)
        return ginivalues

    def split(self, node, node_options, depth, X, y):
        ginivalues = self.gini_all(node_options)
        splitting_on = node_options.columns[ginivalues.index(min(ginivalues))]
        if len(node_options) <= 1 or depth >= self.max_depth:
            X = X[X[splitting_on] == X[splitting_on].mode()[0]]
            return Node(value=X.loc[:, y].mode()[0])
        else:
            # remove that option
            node_options = [option for option in node_options if option != splitting_on]
            node = Node(feature=splitting_on)
            # grow on left and split on it
            depth += 1
            X_left = X[X[splitting_on] == X[splitting_on].mode()[0]]
            node.left = self.split(node.left, node_options, depth, X_left, y)
            # grow on right and split on it
            X_right = X[X[splitting_on] != X[splitting_on].mode()[0]]
            node.right = self.split(node.right, node_options, depth, X_right, y)
            return node

    def predict(self, X):
        pass


data = pd.read_csv("train.csv")

dt = DecisionTree(data)
dt.tree_builder()
