# Python Data Analysis & ML Cheat Sheet
# Comprehensive guide with comments, examples, and practical steps

# ------------------------------
# 1. IMPORTING LIBRARIES
# ------------------------------
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# ------------------------------
# 2. IMPORTING DATA
# ------------------------------
# CSV, Excel, JSON, clipboard

# CSV
df = pd.read_csv('file.csv')

# Excel
df = pd.read_excel('file.xlsx')

# JSON
df = pd.read_json('file.json')

# From clipboard (e.g., copied from Excel)
df = pd.read_clipboard()

# Display top rows
print(df.head())

# ------------------------------
# 3. BASIC DATA EXPLORATION
# ------------------------------
df.shape                # (rows, columns)
df.info()               # Data types and non-null counts
df.describe()           # Summary statistics
df.columns              # Column names
df.dtypes               # Data types
df.nunique()            # Unique values per column
df.duplicated().sum()   # Duplicate rows

# ------------------------------
# 4. CLEANING DATA
# ------------------------------
# Handling missing values
df.isnull().sum()       # Count NaNs
df.dropna(inplace=True) # Drop missing rows
value = "Some Value eg. mean"
df.fillna(value, inplace=True) # Fill NaNs with value

# Example: fill numeric NaN with mean
df['col'] = df['col'].fillna(df['col'].mean())

# Replacing values
df['col'].replace({'old': 'new'}, inplace=True)

# Removing duplicates
df.drop_duplicates(inplace=True)

# ------------------------------
# 5. DATETIME HANDLING
# ------------------------------
df['date_col'] = pd.to_datetime(df['date_col'])
df['month'] = df['date_col'].dt.month
df['dayofweek'] = df['date_col'].dt.dayofweek
df['year'] = df['date_col'].dt.year

# ------------------------------
# 6. FILTERING AND SORTING
# ------------------------------
df[df['col'] > 100]
df.sort_values(by='col', ascending=False)

# ------------------------------
# 7. FEATURE ENGINEERING
# ------------------------------
df['new_col'] = df['col1'] + df['col2']

# Label Encoding
le = LabelEncoder()
df['category_encoded'] = le.fit_transform(df['category'])

# One-hot Encoding
df = pd.get_dummies(df, columns=['category'])

# ------------------------------
# 8. DATA VISUALIZATION
# ------------------------------
sns.histplot(df['col'])
sns.boxplot(x='col', data=df)
sns.heatmap(df.corr(), annot=True)
plt.scatter(df['x'], df['y'])
plt.show()

# ------------------------------
# 9. TRAIN/TEST SPLIT
# ------------------------------
X = df.drop('target', axis=1)
y = df['target']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# ------------------------------
# 10. SCALING
# ------------------------------
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# ------------------------------
# 11. MACHINE LEARNING MODELS
# ------------------------------
# Linear Regression (for continuous targets)
model = LinearRegression()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

# Logistic Regression (for classification)
model = LogisticRegression()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

# Random Forest Classifier
model = RandomForestClassifier(n_estimators=100)
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

# ------------------------------
# 12. EVALUATION
# ------------------------------
print(accuracy_score(y_test, y_pred))
print(confusion_matrix(y_test, y_pred))
print(classification_report(y_test, y_pred))

# ------------------------------
# 13. SAVING & LOADING MODELS
# ------------------------------
import joblib
joblib.dump(model, 'model.pkl')
model = joblib.load('model.pkl')

# ------------------------------
# 14. PRACTICAL TIPS
# ------------------------------
# Checking memory usage
df.memory_usage(deep=True)

# Sampling data
df.sample(frac=0.1)

# Renaming columns
df.rename(columns={'old': 'new'}, inplace=True)

# Apply functions
df['col'] = df['col'].apply(lambda x: x*2)

# Convert column to category
df['col'] = df['col'].astype('category')

# END OF CHEAT SHEET
