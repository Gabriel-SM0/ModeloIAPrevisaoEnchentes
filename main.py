import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, f1_score, confusion_matrix


def analiseDataSheet(datasheet, target):

    #Plan to work

    #1. Load the data
    df = pd.read_csv(datasheet, sep=';')
    print(f"Data loaded successfully for {datasheet} with target variable '{target}'")
    print("Dataset first 5 rows: ")
    print(df.head()) 
    #print the first 5 rows of the dataset to check if it was loaded correctly

    #2. Prepare the data

    df = df.dropna(axis=1, how='any')
    #drop any collums that contains missing values

    #x i use for training the model helping me to understand the relationship between the features and the target variable
    X = df.drop(columns=[target])

    #y is the target variable, the one we want to predict based on the features in X
    y = df[target]


    #3. Pre process data (remove unused columns, handle missing values, encode categorical variables, etc.)
    # On a first look, the local doesnt make sense. But testing the model we can see a improvement like from .60 to .65. So we keep it.
    #X = X.drop(columns=["local"]) 

    # removing the "data" means "date" column, which is likely not useful for the model and may contain non-numeric
    # values that could cause issues during training. 
    # btw, or model need to colect the data in live, and evaluete the risk, 
    # so the "data" column is not useful for training the model, but it can be used to collect data in live and evaluate the risk in real time.
    X = X.drop(columns=["data"]) 

    #Refined table:
    print("\n\nRefined table after removed -local-, -data- and columns with missing valures:")
    print(X.head()) 

    #3.1 Convert data
    X = pd.get_dummies(X)
    # get_dummies is a function in pandas that converts categorical variables into dummy/indicator variables.
    # our csv model contains data like field ("lama" -> mud, "dry"-> seco, "wet"-> molhado), and get_dummies will convert these categorical variables into binary coluumns

    #4. Convert boolean types

    X = X.astype(int) 
    #if some boolean values result from the get_dumies, here we convert them to integers (0 and 1)


    #5. Splitting data into training and testing sets
    #test suze is like 20%
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2) 


    #6. Train the model an do predictions

    model = RandomForestClassifier(class_weight='balanced', n_estimators=200)
    # using randon forest classifier, which is an ensemble learning method that combines multiple decision trees to improve the accuracy and robustness of the model.
    # Class_wheight balanced was used to try to improve the acuracy with the dataset_t, because we saw on the firts try with the confusion matriz that our classes were unbalanced,
    # making our acuracy aroud .39. Ather this adjust with the n_estimators improved, we went from .39 to .43



    #  Above we are training the model using the training data (X_train and y_train) and then making predictions on the test data (X_test)
    #  to evaluate the model's performance.
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)


    #6. Evaluate the model

    print("\n\n")
    print("Model evaluation:")
    print(f"\nFor the dataset {datasheet}, the found results are:")
    print("Acurácia:", accuracy_score(y_test, y_pred))
    print("F1:", f1_score(y_test, y_pred, average='weighted'))
    print("Matriz:\n", confusion_matrix(y_test, y_pred))
    print("\n\n")

    return


analiseDataSheet("dataset_m.csv", "risco")
analiseDataSheet("dataset_t.csv", "prioridade")
