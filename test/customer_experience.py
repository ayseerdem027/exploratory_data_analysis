import pandas as pd
from dotenv import load_dotenv
import matplotlib.pyplot as plt
import os
from sklearn.preprocessing import LabelEncoder
load_dotenv()

file_path = os.getenv("file_path_custmr_exp")
df = pd.read_csv(file_path)
# print(f"Rows, Cols: {df.shape}")
# print(f"Column names: {df.columns}")
# print(f"Sum of duplicated vals: {df.duplicated().sum()}")
print(f"{df.isnull().sum()}")


le = LabelEncoder()
for col in df.columns:
    if df[col].dtype == 'object':
        df[col] = le.fit_transform(df[col])
        
#print(f"Data types after encoding: {df.dtypes}")
#print(f"Data types after encoding: {df.dtypes}")
for col in df.columns:
    if df[col].isnull().any():
        df[col] = df[col].fillna(df[col].mean())
print(df.isnull().sum())

print(df.describe())

cols_x = df[["Age", "Gender", "Products_Purchased"]]
col_y = df["Satisfaction_Score"]
for col in cols_x.columns:
    plt.scatter(df[col], col_y, label=col)
plt.xlabel("Feature Value")
plt.ylabel("Satisfaction Score")
plt.legend()
plt.show()