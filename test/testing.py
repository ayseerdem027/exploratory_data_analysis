import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.preprocessing import LabelEncoder, StandardScaler


class RandomForest:
    
    def main(self, file_name):
    
        # Step 1: Load the data
        # Assume you have a CSV file with customer data
        data = pd.read_csv(file_name)

        # Step 2: Preprocessing
        # Let's assume the target is 'Churn' (Yes/No), and we have some categorical features
        categorical_cols = ['gender', 'part_time_job', 'diet_quality', 'parental_education_level', 'mental_health_rating']
        label_encoders = {}

        # Encode categorical features
        for col in categorical_cols:
            le = LabelEncoder()
            data[col] = le.fit_transform(data[col])
            label_encoders[col] = le

        # Encode target column
        data['extracurricular_participation'] = data['extracurricular_participation'].map({'Yes': 1, 'No': 0})

        # Separate features and target
        X = data[categorical_cols]
        y = data['extracurricular_participation']

        # Optional: Scale numeric features
        scaler = StandardScaler()
        X_scaled = scaler.fit_transform(X)

        # Step 3: Train-test split
        X_train, X_test, y_train, y_test = train_test_split(
            X_scaled, y, test_size=0.2, random_state=42
        )

        # Step 4: Train Random Forest model
        rf = RandomForestClassifier(n_estimators=100, max_depth=10, random_state=42)
        rf.fit(X_train, y_train)

        # Step 5: Evaluate the model
        y_pred = rf.predict(X_test)

        print("Confusion Matrix:")
        print(confusion_matrix(y_test, y_pred))

        print("\nClassification Report:")
        print(classification_report(y_test, y_pred))

        # Optional: Feature importance
        importances = pd.Series(rf.feature_importances_, index=categorical_cols)
        print("\nTop Important Features:")
        print(importances.sort_values(ascending=False).head(10))
        
if __name__ == "__main__":
    rf = RandomForest()
    rf.main("data_analysis/Performance.csv")
    
        
