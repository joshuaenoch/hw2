import pandas as pd
from decision_tree import DecisionTree
from metric_evaluation import MetricEvaluation

# load csv and prepare data
X = pd.read_csv("train.csv")
y = "Survived"

# instantiate tree and create model
dt = DecisionTree(10, 90)
dt.tree_builder(X, y)
y_pred = dt.predict(X)

# evaluate metrics of model 
metric = MetricEvaluation(X[y].to_numpy(), y_pred)
# accuracy 
acc = metric.accuracy_score()
print("Accuracy: ", acc, "%")
# precision 
prec = metric.precision_score()
print("Precision: ", prec, "%")
# recall
rec = metric.recall_score()
print("Recall: ", rec, "%")
# F1
f1 = metric.f1_score()
print("F1 Score: ", f1, "%")