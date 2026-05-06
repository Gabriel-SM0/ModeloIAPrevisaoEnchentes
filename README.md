# Disaster Response Multi-Agent System (ML)

This project focuses on building machine learning classification models for a multi-agent disaster response system, inspired by real-world climate events in Rio Grande do Sul, Brazil.
The main objective is to train a model capable of predicting risk based on external data.

## 🧠 Overview

The system is composed of multiple agents responsible for different tasks:

* **Monitoring Agent (Reactive):** Detects obstacles and maps the environment using sensor data.
* **Triage Agent (Reactive):** Processes and classifies victim-related data from multiple sources.

This repository implements and evaluates classification models for these agents using provided datasets.

---

## 📊 Objectives

* Train and test a classification model for the **monitoring agent**
* Train and test a classification model for the **triage agent**
* Evaluate models using:

  * Accuracy
  * F1 Score
  * Confusion Matrix

---

## 🗂️ Datasets

* `dataset_m.csv` → Monitoring agent
* `dataset_t.csv` → Triage agent

---

## ⚙️ Tech Stack

* Python
* Pandas
* Scikit-learn

---

## 🚀 How to Run

### 1. Clone the repository

```bash
git clone git@github.com:your-username/your-repo.git
cd your-repo
```

### 2. Create and activate virtual environment

```bash
python -m venv venv
```

#### Windows (PowerShell)

```bash
venv\Scripts\Activate.ps1
```

#### Linux / Mac

```bash
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the project

```bash
python main.py
```

---

## 📈 Output

The project generates evaluation metrics for each model, including:

* Accuracy
* F1 Score
* Confusion Matrix

---

## 📌 Notes

* Make sure datasets are correctly placed in the project directory
* Preprocessing is required before training the models

---

## 👥 Authors

Developed as part of an academic project for Artificial Intelligence and Machine Learning, created by Gabriel Silveira and Paola Cardoso.


## Results

Data loaded successfully for dataset_m.csv with target variable 'risco'
Dataset first 5 rows: 
               data  local  velocidade_vento    terreno  correnteza  visibilidade  obstaculos  risco
0  23/12/2021 14:46      0                39       seco          72            20        True      3
1  17/03/2021 08:38     43                53       seco          57            74        True      3
2  12/04/2026 16:13     25                16    telhado          67            21        True      4
3  16/04/2020 16:36     36                24  navegavel          78            96       False      1
4  06/09/2023 20:00     22                53  navegavel          28            54        True      2


Refined table after removed -local-, -data- and columns with missing valures:
   local  velocidade_vento    terreno  correnteza  visibilidade  obstaculos
0      0                39       seco          72            20        True
1     43                53       seco          57            74        True
2     25                16    telhado          67            21        True
3     36                24  navegavel          78            96       False
4     22                53  navegavel          28            54        True



Model evaluation:

For the dataset dataset_m.csv, the found results are:
Acurácia: 0.93
F1: 0.9211433631021844
Matriz:
 [[ 3  0  0  0  0  0]
 [ 0 31  1  0  0  0]
 [ 0  0 68  0  0  0]
 [ 0  0  0 62  1  0]
 [ 0  0  0  5 20  0]
 [ 0  0  0  0  7  2]]



Data loaded successfully for dataset_t.csv with target variable 'prioridade'
Dataset first 5 rows: 
               data  local  risco  n_pessoas     origem  espera  vulneraveis  necessita_medico  nivel_aguasentimento  confiavel  prioridade nivel_agua sentimento
0  23/12/2021 14:46      0      3          2        190     104        False             False                   NaN       True           3    cintura     panico
1  17/03/2021 08:38     43      3          5  instagram     115        False             False                   NaN       True           2  tornozelo      calmo
2  12/04/2026 16:13     25      4          2  instagram      78        False             False                   NaN      False           2  tornozelo      calmo
3  16/04/2020 16:36     36      1          1  instagram      30        False             False                   NaN       True           0  tornozelo    nervoso
4  06/09/2023 20:00     22      2          2  instagram     115        False             False                   NaN       True           2  tornozelo     panico


Refined table after removed -local-, -data- and columns with missing valures:
   local  risco  n_pessoas     origem  espera  vulneraveis  necessita_medico  confiavel nivel_agua sentimento
0      0      3          2        190     104        False             False       True    cintura     panico
1     43      3          5  instagram     115        False             False       True  tornozelo      calmo
2     25      4          2  instagram      78        False             False      False  tornozelo      calmo
3     36      1          1  instagram      30        False             False       True  tornozelo    nervoso
4     22      2          2  instagram     115        False             False       True  tornozelo     panico



Model evaluation:

For the dataset dataset_t.csv, the found results are:
Acurácia: 0.645
F1: 0.630313806777217
Matriz:
 [[11  6  2  4  5  2  0  0]
 [ 1 30  2  0  0  0  0  0]
 [ 1  4 28  2  0  0  0  0]
 [ 2  0  9 34  3  0  0  0]
 [ 2  0  0 13 14  4  0  0]
 [ 1  0  0  1  5  9  0  0]
 [ 0  0  0  0  0  1  3  0]
 [ 0  0  0  0  0  0  1  0]]


## Conclusion
This project focused on developing machine learning models for a monitoring agent and a triage agent within a flood response system. Both models were built using a Random Forest classifier and followed a structured pipeline including data preprocessing, training, and evaluation. The monitoring model achieved strong results from the beginning, due to the presence of clear and objective environmental features directly related to risk prediction.

The triage model initially showed lower performance due to more complex and less structured data. However, after refining preprocessing steps, balancing the dataset, and including additional relevant features such as location, the model improved significantly, reaching satisfactory performance levels. Overall, the results demonstrate the importance of data preparation and feature selection, as well as the effectiveness of machine learning in supporting decision-making in real-world scenarios.

These results reinforce the relevance of machine learning in complex, real-world disaster scenarios, especially when supported by proper data preparation and feature engineering.

