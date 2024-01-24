import numpy as np
import pandas as pd
from sklearn import ensemble
from sklearn.model_selection import train_test_split

def main():
    df = pd.read_csv("information.csv")
    feature_names = ['NDVI', 'Drought', 'Elevation', 'DSMP']
    label = "Landcover"
    X = df[feature_names]
    y = df[label]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    n_trees = 500
    rf = ensemble.RandomForestClassifier(n_trees).fit(X_train, y_train)
    predictions = rf.predict(X_test)
    errors = abs(predictions - y_test)
    num=0
    for i in errors:
        if i==0:
            num+=1
    print("The random forest algorithm has a "+str(num*100/len(errors))+" of success rate")
    return rf