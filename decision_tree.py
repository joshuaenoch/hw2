# 1. Write a function to calculate impurity (e.g., Shannon entropy or Gini index).
# 2. Implement a recursive function to split data based on impurity reduction and grow the tree.
# 3. Set stopping conditions to prevent infinite recursion (e.g., max depth, min samples per split, pure nodes).
from collections import Counter
class DecisionTree:
    # we might need hyperparamters based on the rubric, like max-depth
    def __init__(self, data, ):
        #self.head = Node
        #self.data = data #training data passed into fit
        self.root = None #acts as root node, will use this to build tree in fit()
        pass

    def fit(self, X, y):
        self.root = self.tree_builder(X, y)

    # tree builder makes calls to our split() method
    # this method will use recursion to build our tree
    def tree_builder(self, X, y):
        pass

    def gini(self,n, total):
            return ((n**2) / (total**2))

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

    # anthony is going to finish this but its complete  rn
    def why_did_I_do_this(self):
        self.ginivalues = {}
        ans = 1
        counter = Counter(self.data)
        for x in counter:
            ans = ans -(x / len(counter))


    def split(self, node, node_options):
        if node.isleaf():
            return
        else:
            # get the best option
            splitting_on = self.gini_all(node_options)
            # remove that option
            node_options = node_options.remove(splitting_on)
            # grow on left and split on it
            node.left = Node(values=splitting_on.options[0])
            self.split(node.left, node_options)
            # grow on right and split on it
            node.left = Node(values=splitting_on.options[1])
            self.split(node.right, node_options)


    def isleaf():
        pass

    def predict(self, X):
        pass

class Node():
    def __init__(self, feature=None, threshold=None, left=None, right=None, values=None, options=None, gini=None):
        self.feature = feature
        self.threshold = threshold
        self.left = left
        self.right = right
        self.values = values
        self.options = options
        self.gini = gini

    def dealWithNonBinary(self, ):
        pass