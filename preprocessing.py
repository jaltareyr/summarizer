import pandas as pd
import numpy as np
import json
from sklearn.model_selection import train_test_split

with open("assets/data/reviews_data.json", "r") as file:
    data = json.load(file)

X = []
y = []

for cat in data:
    for item in data[cat]:

        X.append(data[cat][item]['rev'][0])
        X.append(data[cat][item]['rev'][0])
        X.append(data[cat][item]['rev'][0])

        y.append(' '.join(data[cat][item]['gold_summs'][0][0]).strip())
        y.append(' '.join(data[cat][item]['gold_summs'][0][1]).strip())
        y.append(' '.join(data[cat][item]['gold_summs'][0][2]).strip())

df = pd.DataFrame({
    'X': X,
    'y': y
})

def format_X(val):
    output = [] 
    for line in val:
        output.append(' '.join(line))
    return ' '.join(output)

df["X"] = df["X"].apply(format_X)

X =  ["Summarize: " + seq for seq in list(df['X'])]
y = list(df['y'])

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
X_train, X_eval, y_train, y_eval = train_test_split(X_train, y_train, test_size=0.25, random_state=40)

pd.DataFrame(X_train, columns=["X"]).to_csv("assets/data/X_train.csv")
pd.DataFrame(y_train, columns=["y"]).to_csv("assets/data/y_train.csv")

pd.DataFrame(X_test, columns=["X"]).to_csv("assets/data/X_test.csv")
pd.DataFrame(y_test, columns=["y"]).to_csv("assets/data/y_test.csv")

pd.DataFrame(X_eval, columns=["X"]).to_csv("assets/data/X_eval.csv")
pd.DataFrame(y_eval, columns=["y"]).to_csv("assets/data/y_eval.csv")