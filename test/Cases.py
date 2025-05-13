import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
import numpy as np
import logging
# this is a test file
# this is a test file
# this is a test file
class Cases:
    def __init__(self, file_name):
        self.file = file_name
        self.df = None
   
    def read_csv(self):
        try:
            self.df = pd.read_csv(self.file, encoding="latin1")
        except FileNotFoundError:
            logging.error(f"File: {self.file} not found")
            
    def plot_cases_by_country(self):
        if self.df is None or self.df.empty:
            logging.error("Dataframe is empty or null")
            return
        plt.figure(figsize=(8, 5))
        
        grouped_df = self.df[self.df['Entity'].str.startswith('G', na=False)].groupby(['Entity'], dropna=True)['Cases'].sum().reset_index()
        sns.scatterplot(data=grouped_df, x='Entity', y='Cases')
        plt.show()
    def get_case_by_country(self):
        if self.df.empty:
            logging.error("Dataframe is empty")
            return
        filtered_df = self.df.groupby(['Entity'])['Cases'].sum()
        plt.plot(filtered_df.index, filtered_df.values, 'ro')
        plt.show()
        
    def main(self):
        self.read_csv()
        #self.plot_cases_by_country()
        self.get_case_by_country()
        
if __name__ == "__main__":
    case = Cases("Cases.csv")
    case.main()