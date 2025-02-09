# draft of deicison
# TODO:
# - fit method
# - series from .mode issue

import pandas as pd
from collections import Counter
from metric_evaluation import MetricEvaluation

# nodes for the decision tree that carries information for predictions
class Node:
    def __init__(
        self,
        feature=None,  # the attribute
        threshhold=None,  # the value of the attribute splitting on
        left=None,
        right=None,
        value=None,  # only for leaf nodes, the prediction value
        attribute_type="object",  # the type the values of the attribute are
    ):
        self.feature = feature
        self.threshhold = threshhold
        self.left = left
        self.right = right
        self.value = value
        self.attribute_type = attribute_type


class DecisionTree:
    # initializer
    def __init__(self, max_depth=None, min_samples_split=None):
        self.root = None
        self.max_depth = max_depth
        self.min_samples_split = min_samples_split

    # tree builder makes calls to our split() method
    # this method will use recursion to build our tree
    def tree_builder(self, X, y, depth=0):
        # gets all the features to split on (excludes the target variable)
        node_options = [col for col in X.columns if col != y]
        # creates the tree including the root node
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

    # recursive method to build the tree
    def split(self, node, node_options, depth, X, y):
        # takes in the gini values of all remaining features of data
        ginivalues = self.gini_all(node_options, X)
        
        # break if no gini values
        if len(ginivalues) <= 0:
            return None
        
        # selects the attribute to be split on based on gini values
        splitting_on = node_options[ginivalues.index(min(ginivalues))]

        # the threshhold is the value of the attribute to be split based on

        # handling different data types (categorical vs continuous)
        attribute_type = X[splitting_on].dtype
        # if the data is categorical, the threshhold is the most common value
        if attribute_type == "object":
            # temporary solution to issue where the mode is not a series
            if not isinstance(X[splitting_on].mode(), pd.Series):
                threshhold = X[splitting_on].mode()
            else:
                threshhold = X[splitting_on].mode()[0]
        # if the data is continuous, the threshhold is the mean of all values
        else:
            threshhold = X[splitting_on].mean()

        # if there are no more attributes or the max depth or minimum rows have
        # been breached, stop splitting and create a leaf node
        if (
            len(node_options) <= 0
            or depth >= self.max_depth
            or len(X) <= self.min_samples_split
        ):
            # there is probably a more efficient way than having to refilter
            # but just in case, do one last split
            if attribute_type == "object":
                X = X[X[splitting_on] == threshhold]
            else:
                X = X[X[splitting_on] < threshhold]
            # temporary solution to issue where the mode is not a series
            value = X[y].mode()
            if isinstance(value, pd.Series):
                if not value.empty:
                    value = value[0]
                else:
                    # there is a bug where the value is still a series, it will
                    # just be set as None for now
                    value = None

            # return the leaf node
            return Node(
                feature=splitting_on,
                threshhold=threshhold,
                value=value,
                attribute_type=attribute_type,
            )

        else:
            # remove the attribute from the attribute options
            node_options = [option for option in node_options if option != splitting_on]
            # create a node (without a value)
            node = Node(
                feature=splitting_on,
                threshhold=threshhold,
                attribute_type=attribute_type,
            )

            depth += 1

            # split the data based on the threshhold of the splitting_on
            # attribute and pass them down to their respective nodes
            if attribute_type == "object":
                X_left = X[X[splitting_on] == threshhold]
                X_right = X[X[splitting_on] != threshhold]
            else:
                X_left = X[X[splitting_on] < threshhold]
                X_right = X[X[splitting_on] > threshhold]
            node.left = self.split(node.left, node_options, depth, X_left, y)
            node.right = self.split(node.right, node_options, depth, X_right, y)

            # return the node
            return node

    # predicting the values of the target variable, returns a list
    # target variable is specified during tree building, not sure if it was
    # supposed to be done here instead
    def predict(self, X):
        # the list of predicted values
        predictions = []

        # predict for each row in X
        for index, row in X.iterrows():

            # traverse the tree until a leaf node is reached
            node = self.root
            # a leaf node does not have a left or right node
            while node.left or node.right:
                # for categorical values, search based on whether the value is
                # the same as the threshhold (most common value)
                if node.attribute_type == "object":
                    if row[node.feature] == node.threshhold:
                        node = node.left
                    else:
                        node = node.right
                # for continuous values, search based on whether the value is
                # below or above the threshhold
                else:
                    if row[node.feature] < node.threshhold:
                        node = node.left
                    else:
                        node = node.right

            # add the prediction to the list
            predictions.append(node.value)

        # return the list
        return predictions


# # testing the tree on train.csv (titanic dataset)
# data = pd.read_csv("train.csv")
# dt = DecisionTree(5, 10)
# y = "Survived"
# dt.tree_builder(data, y)
# y_pred = dt.predict(data)
# #print(y_pred)

# metric = MetricEvaluation(data[y].to_numpy(),y_pred)
# #accuracy
# acc = metric.accuracy_score()
# print("Accuracy: " + str(acc) + "%")
# #precision
# prec = metric.precision_score()
# print("Precision: " + str(prec) + "%")
# #recall 
# rec = metric.recall_score()
# print("Recall: " + str(rec) + "%")
# #f1
# f1 = metric.f1_score()
# print("F1-Score: " + str(f1) + "%")


print("Testing Dummies")
print("=====================")
data = pd.read_csv("train.csv")
features = ["Pclass", "Sex", "SibSp", "Parch", "Age", "Cabin", "Survived"]
X = data[features]
X = pd.get_dummies(X)
y = "Survived"

# build decision tree
dt = DecisionTree(5, 10)
dt.tree_builder(X, y)
y_pred = dt.predict(X)

# evaluate metrics
metric = MetricEvaluation(data[y].to_numpy(),y_pred)
#accuracy
acc = metric.accuracy_score()
print("Accuracy: " + str(acc) + "%")
#precision
prec = metric.precision_score()
print("Precision: " + str(prec) + "%")
#recall 
rec = metric.recall_score()
print("Recall: " + str(rec) + "%")
#f1
f1 = metric.f1_score()
print("F1-Score: " + str(f1) + "%")
