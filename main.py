import pandas as pd
from sklearn.linear_model import LinearRegression

print("Tudo certo")


#Plan to work

#1. Load the data
df = pd.read_csv("dataset.csv")

#2. Prepare the data
X = df.drop(columns=["target"])
y = df["target"]

#3. Pre process data (remove unused columns, handle missing values, encode categorical variables, etc.)
X = X.drop(columns=["data"])

#3.1 Convert data
X = pd.get_dummies(X)

#4. Convert boolean types

X = X.astype(int)  # ou só nas colunas booleanas


#5. Splitting data into training and testing sets
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)


#6. Train the model
from sklearn.ensemble import RandomForestClassifier

model = RandomForestClassifier()
model.fit(X_train, y_train)

#6. Do predictions
from sklearn.ensemble import RandomForestClassifier

model = RandomForestClassifier()
model.fit(X_train, y_train)

#7. Evaluate the model
from sklearn.metrics import accuracy_score, f1_score, confusion_matrix

print("Acurácia:", accuracy_score(y_test, y_pred))
print("F1:", f1_score(y_test, y_pred, average='weighted'))
print("Matriz:\n", confusion_matrix(y_test, y_pred))