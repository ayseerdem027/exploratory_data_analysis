import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import logging
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
import numpy as np


class PriceAnalysis:
    def __init__(self, file_name):
        self.file = file_name
        self.data = None
        self.df = None
    
    def read_file(self):
        try:
            self.df = pd.read_csv(self.file, encoding="latin1")
        except FileNotFoundError:
            logging.error(f"File {self.file} could not be found")
            
    def plot_price_distribution(self):
        if self.df is not None:
            plt.figure(figsize=(8, 5))
            sns.scatterplot(data=self.df, x='bedrooms', y='price')
            sns.regplot(data=self.df, y='price', x='bedrooms')
            plt.xlabel("rooms")
            plt.ylabel("price")
            plt.show()
            
    def correlation(self):
        corr_matrix = self.df.corr(method='spearman', numeric_only=True)
        print(corr_matrix)
        sns.heatmap(corr_matrix, annot=True, cmap='coolwarm')
        plt.show()
        
    def train_multiple_features(self):
        # regression funtion: y = mx + b
        # y is the value, we're predicting eg price
        # m is the increase rate, x is the feature eg area, rooms etc, b is the value of y when x is zero 
        
        x = self.df[['bedrooms', 'bathrooms', 'area', 'parking', 'stories']]
        y = self.df['price']
        x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)
        model = LinearRegression()
        model.fit(x_train, y_train)
        y_pred = model.predict(x_test)
        
        # Evaluate the model
        mse = mean_squared_error(y_test, y_pred)
        r2 = r2_score(y_test, y_pred)
        print(f" Train: Mean Squared Error: {mse}")
        print(f" Train: R² Score: {r2}")
        
    def correlation_price_location(self):
        if self.df.empty:
            logging.error("Dataframe is empty")
            return
        try:
            corr_matrix = self.df.corr(method='spearman', numeric_only=True)
            print(corr_matrix)
            plt.figure(figsize=(8, 5))
            #sns.scatterplot(data=self.df, x='area', y='price')
            sns.regplot(data=self.df, y='price', x='area')
            plt.show()
        except KeyError as e:
            logging.error(f"Key error: {e}. Please check the column names in the DataFrame.")
            
    def train_one_feature(self):
        if self.df.empty:
            logging.error("Dataframe is empty")
            return
        try:
            if 'area' not in self.df.columns:
                logging.error("The 'area' column is missing in the DataFrame.")
                return
            x = self.df['area'].values.reshape(-1, 1)
            y = self.df['price']
            x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)
            model = LinearRegression()
            model.fit(x_train, y_train)
            y_pred = model.predict(x_test)
            mse = mean_squared_error(y_test, y_pred)
            r2 = r2_score(y_test, y_pred)
            print(f"Mean Squared Error: {mse}")
            print(f"R² Score: {r2}")
        except KeyError as e:
            logging.error(f"Key error: {e}. Please check the column names in the DataFrame.")
            
    def training_features(self):
        x = self.df[['bedrooms', 'bathrooms', 'stories', 'area', 'parking']]
        y = self.df['price']
        x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)
        model = LinearRegression()
        model.fit(x_train, y_train)
        y_pred = model.predict(x_test)
        mse = mean_squared_error(y_test, y_pred)
        rmse = np.sqrt(mse)
        r2 = r2_score(y_test, y_pred)
        print(f"Mean Squared Error: {mse}")
        print(f"Root Mean Squared Error: {rmse}")
       # print(f"R² Score: {r2}")
        
    def main(self):
        self.read_file()
        #self.plot_price_distribution()
        #self.correlation()
        #self.correlation_price_location()
        #self.train_one_feature()
        self.train_multiple_features()
        self.training_features()
        
if __name__ == "__main__":
    pa = PriceAnalysis("Housing.csv")
    pa.main()
        
    