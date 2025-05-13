import pandas as pd
import matplotlib.pyplot as plt
import logging

class WthAnalysis:
    def __init__(self, file_name):
        self.file = file_name
        self.data = None
        self.temp_avg = None
        self.temp_min = None
    def read_csv(self):
        try:
            self.data = pd.read_csv(self.file)

        except FileNotFoundError:
            logging.error("Cannot find the file")
    def get_max_temp(self):
        if self.data.empty:
            logging.error(F"No data found to claculate the maximum")
            return
        temp_max = self.data["Temperature_C"].astype(float).max()
        return temp_max
    def get_min_temp(self):
        if self.data.empty:
            logging.error("No data to calculate the minimum")
            return
        temp_min = self.data["Temperature_C"].astype(float).min()
        self.temp_min = temp_min
    def get_avg_temp(self):
        temp_avg = self.data["Temperature_C"].astype(float).mean()
        self.temp_avg = temp_avg
    def plotting_temp(self):
        if self.data.empty:
          logging.error("No data to plot")  
          return
        plt.subplot(131)
        plt.plot(self.data["Date"], self.data["Temperature_C"], 'bs', self.temp_avg, self.temp_min, 'ro')
        plt.ylabel("Temp")
        plt.xlabel("Date")
        plt.subplot(132)
        plt.bar(self.data["Date"], self.data["Temperature_C"])
        plt.show()
        
if __name__ == "__main__":
    wa = WthAnalysis("weather_data.csv")
    wa.read_csv()
    wa.get_min_temp()
    wa.get_max_temp()
    wa.get_avg_temp()
    wa.plotting_temp()