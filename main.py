import os
import pandas as pd
from sklearn.model_selection import train_test_split

# load csv files
find_dir = os.path.dirname(os.path.abspath(__file__))
train_path = os.path.join(find_dir, "train.csv")
train_data = pd.read_csv(train_path)

# select features and target variable
y = train_data["Survived"]
features = ["Pclass", "Sex", "SibSp", "Parch"]
X = pd.get_dummies(train_data[features])
train_X, test_X, train_y, test_y = train_test_split(X, y, test_size=0.1, random_state=1)