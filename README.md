# Disaster Response Multi-Agent System (ML)

This project focuses on building machine learning classification models for a multi-agent disaster response system, inspired by real-world climate events in Rio Grande do Sul, Brazil.

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

Developed as part of an academic project for Artificial Intelligence and Machine Learning, created By Gabriel Silveira and Paola Cardoso.
