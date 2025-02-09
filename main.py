import os
import pandas as pd
from decision_tree import DecisionTree
from metric_evaluation import MetricEvaluation
from sklearn.model_selection import train_test_split

#from sklearn.tree import DecisionTreeClassifier
#from sklearn.metrics import classification_report

# load csv files
train_data = pd.read_csv("train.csv")

# select features and target variable
y = train_data["Survived"]
features = ["Pclass", "Sex", "SibSp", "Parch"]
X = pd.get_dummies(train_data[features])

# split data
train_X, test_X, train_y, test_y = train_test_split(X, y, test_size=0.1, random_state=1)

# instantiate decision tree and create model
dt = DecisionTree()
# dt = DecisionTree()
# preds = dt.predict(test_X)

####################################
## Steps to test/apply metrics
####################################

## use scikit to create a tree to test metric functions
#dt = DecisionTreeClassifier()
#dt.fit(train_X, train_y)
#preds = dt.predict(test_X)
#print(classification_report(test_y,preds))

## display metric evaluations
#metric = MetricEvaluation(test_y.to_numpy(),preds)

#acc = metric.accuracy_score()
#print("Accuracy: " + str(acc) + "%")

#prec = metric.precision_score()
#print("Precision: " + str(prec) + "%")

#rec = metric.recall_score()
#print("Recall: " + str(rec) + "%")

#f1 = metric.f1_score()
#print("F1-Score: " + str(f1) + "%")