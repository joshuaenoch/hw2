import pandas as pd
from collections import Counter


class Node:
    def __init__(
        self,
        feature=None,
        threshhold=None,
        left=None,
        right=None,
        value=None,
        attribute_type="object",
    ):
        self.feature = feature
        self.threshhold = threshhold
        self.left = left
        self.right = right
        self.value = value
        self.attribute_type = attribute_type

    def dealWithNonBinary(
        self,
    ):
        pass


class DecisionTree:
    # we might need hyperparamters based on the rubric, like max-depth
    def __init__(self, max_depth=None, min_samples_split=None):
        self.root = None
        self.max_depth = max_depth
        self.min_samples_split = min_samples_split

    def fit(self, X, y):
        self.root = self.tree_builder(X, y, depth=0)

    # tree builder makes calls to our split() method
    # this method will use recursion to build our tree
    def tree_builder(self, X, y, depth=0):
        node_options = [col for col in X.columns if col != y]
        # print(node_options)
        self.root = self.split(self.root, node_options, depth, X, y)

    def gini(self, n, total):
        return (n**2) / (total**2)

    # anthony is going to finish this but its complete  rn
    def gini_all(self, node_options, X):
        ginivalues = []
        for n in range(len(node_options)):
            counter = Counter(X.iloc[:, n])
            ans = 1
            total = counter.total()
            for x in counter.values():
                ans -= self.gini(x, total)
            ginivalues.append(ans)
        return ginivalues

    def split(self, node, node_options, depth, X, y):
        ginivalues = self.gini_all(node_options, X)
        splitting_on = node_options[ginivalues.index(min(ginivalues))]
        # print(len(node_options))
        # print(splitting_on)
        attribute_type = X[splitting_on].dtype
        # print(splitting_on)
        # print(X[splitting_on].mode()[0])
        # print(X[splitting_on].mode()[0].dtype)
        if attribute_type == "object":
            if not isinstance(X[splitting_on].mode(), pd.Series):
                threshhold = X[splitting_on].mode()
            else:
                threshhold = X[splitting_on].mode()[0]
        else:
            threshhold = X[splitting_on].mean()
        if (
            len(node_options) <= 0
            or depth >= self.max_depth
            or len(X) <= self.min_samples_split
        ):
            if attribute_type == "object":
                X = X[X[splitting_on] == threshhold]
            else:
                X = X[X[splitting_on] < threshhold]

            value = X[y].mode()
            if isinstance(value, pd.Series):
                if not value.empty:
                    value = value[0]
                else:
                    value = None
            return Node(
                feature=splitting_on,
                threshhold=threshhold,
                value=value,
                attribute_type=attribute_type,
            )
        else:
            # remove that option
            node_options = [option for option in node_options if option != splitting_on]
            node = Node(
                feature=splitting_on,
                threshhold=threshhold,
                attribute_type=attribute_type,
            )
            # grow on left and split on it
            depth += 1

            if attribute_type == "object":
                X_left = X[X[splitting_on] == threshhold]
                X_right = X[X[splitting_on] != threshhold]
            else:
                X_left = X[X[splitting_on] < threshhold]
                X_right = X[X[splitting_on] > threshhold]
            node.left = self.split(node.left, node_options, depth, X_left, y)
            # grow on right and split on it
            node.right = self.split(node.right, node_options, depth, X_right, y)
            return node

    def predict(self, X):
        predictions = []
        for index, row in X.iterrows():
            node = self.root
            while node.left or node.right:
                if node.feature:
                    if node.attribute_type == "object":
                        if row[node.feature] == node.threshhold:
                            node = node.left
                        else:
                            node = node.right
                    else:
                        if row[node.feature] < node.threshhold:
                            node = node.left
                        else:
                            node = node.right
            predictions.append(node.value)
        return predictions


data = pd.read_csv("train.csv")

dt = DecisionTree(5, 10)
y = "Survived"
dt.tree_builder(data, y)
y_pred = dt.predict(data)
print(y_pred)
