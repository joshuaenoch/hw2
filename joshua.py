# 1. Write a function to calculate impurity (e.g., Shannon entropy or Gini index).
# 2. Implement a recursive function to split data based on impurity reduction and grow the tree.
# 3. Set stopping conditions to prevent infinite recursion (e.g., max depth, min samples per split, pure nodes).

import pandas as pd


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
        self.data = data

    def fit(self):
        self.root = self.tree_builder()

    # tree builder makes calls to our split() method
    # this method will use recursion to build our tree
    def tree_builder(self):
        self.root = Node()
        node_options = self.data.columns
        self.split(self.root, self.data, node_options, 0)

    def gini(self, n, total):
        pass

    def gini_all(self, options):
        order = options
        for i in range(len(options)):
            order[i] = gini(options[i].n, options[i].total)
        return order

    def split(self, node, node_options, depth):
        if len(node_options) <= 1:
            node.left = Node(node_options[0])
        else:
            # get the best option
            splitting_on = gini_all(node_options)
            if depth >= self.max_depth:
                node.left = Node(splitting_on)
            else:
                depth += 1
                # remove that option
                node_options = node_options.remove(splitting_on)
                # grow on left and split on it
                node.left = Node(values=splitting_on.options[0])
                split(node.left, node_options, depth)
                # grow on right and split on it
                node.left = Node(values=splitting_on.options[1])
                split(node.right, node_options, depth)

    def predict(self, X):
        pass


data = pd.read_csv("train.csv")

