import matplotlib.pyplot as plt
import pandas as pd
import logging

class SalAnalysis:
    def __init__(self, file_name):
        self.data = None
        self.file = file_name
    
    def read_csv(self):
        try:
            self.data = pd.read_csv(self.file, encoding="latin1")
        except FileNotFoundError:
            logging.error(f"File could not be found {self.file}")
    def get_total_sales(self):
        sales_by_month = self.data.groupby(['MONTH_ID'], dropna=True)['SALES'].sum()
        plt.plot(sales_by_month.index, sales_by_month.values, marker='o', linestyle='-', color='b')
        plt.xlabel("Month")
        plt.ylabel("Total Sales")
        plt.grid(True)
        plt.show()
    def get_avg_sales(self):
        avg_sales_by_month = self.data.groupby(['MONTH_ID'], dropna=True)['SALES'].mean()
        plt.plot(avg_sales_by_month.index, avg_sales_by_month.values, marker='o', linestyle='-', color='b')
        plt.grid(True)
        plt.show()
        
    def get_min_sales(self):
        min_sales_by_month = self.data.groupby(['MONTH_ID'], dropna=True)['SALES'].min()
        print(min_sales_by_month)
        index = min_sales_by_month.idxmin()
        low_sales_months = min_sales_by_month[min_sales_by_month < 600].index.tolist()
        print(f"Months with sales lower than 600: {low_sales_months}")
        plt.plot(min_sales_by_month.index, min_sales_by_month.values, 'bs')
        plt.grid(True)
        plt.show()
    def get_top_customer_by_sales(self):
        sum_customers_by_sales = self.data.groupby(['CUSTOMERNAME'], dropna=True)['SALES'].sum()
        top_customer = sum_customers_by_sales.idxmax()
        print(sum_customers_by_sales)
    def get_top_country_by_sales(self):
        if self.data is not None:
            sum_countries_by_sales = self.data.groupby(['COUNTRY'])['SALES'].sum()
            min_sum_country = sum_countries_by_sales.min()
            high_sales_countries = sum_countries_by_sales[sum_countries_by_sales > 10*min_sum_country]
            plt.plot(high_sales_countries.index, high_sales_countries.values, 'ro')
            plt.grid(True)
            plt.show()
            print(high_sales_countries)
        else:
            logging.error("Data is not loaded. Please check the CSV file.")
    def get_prodcutline_with_highest_sales(self):
        highest_sales_line = self.data.groupby(['PRODUCTLINE'])['SALES'].sum()
        max_line = highest_sales_line.idxmax()
        print(max_line)
        
    def get_average_of_every_state(self):
        if self.data.empty:
            return
        average_by_state = self.data.groupby('COUNTRY', dropna=True)['SALES'].mean()
        print(average_by_state)   
        
    def main(self):
        self.read_csv()
        #self.get_top_country_by_sales()
        #self.get_top_customer_by_sales()
        self.get_average_of_every_state()
        
class ElecAnalysis:
    def __init__(self, file_name):
        self.data = None
        self.file = file_name
        
    def read_csv(self):
        try:
            self.data = pd.read_csv(self.file, encoding="latin1")
            #print(self.data.head())
        except FileNotFoundError:
            logging.error(f"File could not be found {self.file}")
    def get_nuc_usage_by_country(self):
        if self.data.empty:
            return
        nuc_usage_by_country = self.data.groupby(['State'], dropna=True)['Nuclear_MW'].sum()
        top_country = nuc_usage_by_country.idxmax()
        plt.plot(nuc_usage_by_country.index, nuc_usage_by_country.values, 'ro')
        plt.ylabel("Solar_wm")
        plt.xlabel("state")
        plt.grid(True)
        #plt.show()
        #print(top_country)
    def get_least_nuc_usage_by_country(self):
        if self.data.empty:
            return
        least_nuc_usage = self.data.groupby('State', dropna=True)['Nuclear_MW'].sum()
        min_usage_state = least_nuc_usage.idxmin()
        print(min_usage_state)
    def get_most_nuc_usage_by_country(self):
        if self.data.empty:
            logging.error("Data is empty")
            return
        nuc_usage_by_country= self.data.groupby('State', dropna=True)['Nuclear_MW'].sum()
        max_usage_by_country = nuc_usage_by_country.idxmax()
        print(max_usage_by_country)

        
    def main(self):
        self.read_csv()
        #self.get_nuc_usage_by_country()
        #self.get_least_nuc_usage_by_country()
if __name__ == "__main__":
    #ea = ElecAnalysis("Power_Plants.csv")
    #ea.main()
    sa = SalAnalysis("sales_data_sample.csv")
    sa.main()