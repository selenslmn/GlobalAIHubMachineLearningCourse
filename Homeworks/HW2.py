# Homework 2

from sklearn.datasets import load_diabetes
import pandas as pd
X , y = load_diabetes(return_X_y=True)
df = pd.DataFrame(X,columns = load_diabetes().feature_names)
df.head()
df.info()
df.describe()
df.isna().sum()
