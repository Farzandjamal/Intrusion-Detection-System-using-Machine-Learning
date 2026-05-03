#_______________Data-Preprocessing____________#
import pandas as pd
import numpy as np
df=pd.read_parquet('Benign-Monday-no-metadata.parquet')
#print(df.columns)
#Lets Remove unecessary coulmns
#df=df.drop(columns=['Label'])
#these contains low value.
df = df.drop(columns=[
    'Fwd Avg Bytes/Bulk',
    'Fwd Avg Packets/Bulk',
    'Fwd Avg Bulk Rate',
    'Bwd Avg Bytes/Bulk',
    'Bwd Avg Packets/Bulk',
    'Bwd Avg Bulk Rate'
])
#these are redundandt colmuns
df = df.drop(columns=[
    'Avg Fwd Segment Size',
    'Avg Bwd Segment Size',
    'Subflow Fwd Packets',
    'Subflow Fwd Bytes',
    'Subflow Bwd Packets',
    'Subflow Bwd Bytes'
])
#weak flags 
df = df.drop(columns=[
    'Fwd URG Flags',
    'Bwd URG Flags',
    'CWE Flag Count'
])
#print('this is cleaner model columns now!')
#print(df.info())
#print(df.isnull().sum())
#print(np.isinf(df).sum())
#----------transform------------
#Assigns  Data to X and Y 
x=df.drop('Label',axis=1)
y=df['Label']
from sklearn.preprocessing import StandardScaler
scaler=StandardScaler()
x_scaled=scaler.fit_transform(x)

#__________Lets Train The Data___________#
from sklearn.ensemble import IsolationForest
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report,confusion_matrix
model = IsolationForest(
    n_estimators=200,
    max_samples=0.8,
    contamination=0.02,   # adjust later
    random_state=42
)

model.fit(x_scaled)
#print('model has been trained!')
#________Testing Stage___________#

df_test = pd.read_parquet("final_test_dataset.parquet")
#split to x and y
X_test = df_test.drop('Label', axis=1)
y_test = df_test['Label']
#scaled
X_test_scaled = scaler.transform(X_test)
#predict
y_pred = model.predict(X_test_scaled)
#readable format!0=normal and 1=attack
y_pred = np.where(y_pred == 1, 0, 1)   
y_test = np.where(y_test == 'Benign', 0, 1)
#Evaluation of Model
from sklearn.metrics import classification_report, confusion_matrix

print(confusion_matrix(y_test, y_pred))
print(classification_report(y_test, y_pred))
#print(df_test['Label'].value_counts())



