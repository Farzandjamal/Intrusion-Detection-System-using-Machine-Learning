# Intrusion-Detection-System-using-Machine-Learning
Anomaly-based Intrusion Detection System using Machine Learning (Isolation Forest) on CIC-IDS2017 dataset.
# 🛡️ Intrusion Detection System using Machine Learning

## 📌 Project Description
This project implements an anomaly-based Intrusion Detection System (IDS) using Machine Learning.  
The system uses the Isolation Forest algorithm to detect abnormal network traffic patterns.

The model is trained on normal (benign) traffic and tested on mixed traffic containing both benign and attack data.

## 📊 Dataset
CIC-IDS2017 (Canadian Institute for Cybersecurity dataset)

It includes real-world network traffic with multiple attack types such as:
- DoS / DDoS
- Botnet
- Port Scan
- Web Attacks (SQL Injection, XSS, Brute Force)

## 🤖 Machine Learning Model
- Algorithm: Isolation Forest  
- Type: Unsupervised Anomaly Detection  

## 🧠 Workflow
1. Data Preprocessing
2. Feature Scaling
3. Model Training (on benign traffic)
4. Testing on mixed dataset
5. Evaluation using classification metrics

## 📈 Results
- Accuracy: ~93%
- Attack Recall: ~73–77%
- Precision: ~75–80%
- F1-score: ~75%

## 🛠️ Technologies Used
- Python
- Pandas
- NumPy
- Scikit-learn

## 📁 Project Structure
- train.py
- test.py
- preprocessing script
- dataset files (optional/sample)

## 🚀 How to Run
```bash
pip install -r requirements.txt
python train.py
python test.py

