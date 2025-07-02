class WeatherAnalysis:
    def __init__(self, file_name):
        self.file_name = file_name
        self.lines = []
        self.data = []
        
    def ReadCSV(self):
        try:
            with open(self.file_name, "r") as file:
                lines = file.readlines()
            self.lines = lines
        except FileNotFoundError:
            print(f"Error: The file '{self.file_name}' was not found.")
            self.lines = []
        
    def ParseCSV(self):
        data = []
        for line in self.lines[1:]:
            parts = line.strip().split(",")
            if len(parts) == 3:
                date, temperature, humidity = parts
                data.append({
                    "date": date,
                    "temperature": float(temperature),
                    "humidity": float(humidity)
                })
        self.data = data
    
    def CalculateMaxTemp(self):
        max_temp = 0
        for entry in self.data:
            if entry["temperature"] > max_temp:
                max_temp = entry["temperature"]
                max_date = entry["date"]
        if max_date:
            print(f"The maximum temperature was {max_temp} on {max_date}.")
        else:   
            print("No valid temperature data found.")
    
    def CalculateMinTemp(self):
        min_temp = float('inf')
        for entry in self.data:
            if entry["temperature"] < min_temp:
                min_temp = entry["temperature"]
                min_date = entry["date"]
        if min_date:
            print(f"The minimum temperature was {min_temp} on {min_date}.")
        else:   
            print("No valid temperature data found.")
            
    def CalculateTheAverageTemp(self):
        total_temp = 0
        count = 0    
        for entry in self.data:
            if entry["temperature"]:
                total_temp += entry["temperature"]
                count += 1
        if count > 0:
            average_temp = total_temp / count
            print(f"The average temperature is {average_temp}.")
        else:
            print("No valid temperature data found.")
        
    def main(self):
         self.ReadCSV()
         self.ParseCSV()
         self.CalculateMaxTemp()
         self.CalculateMinTemp()
         self.CalculateTheAverageTemp()
if __name__ == "__main__":
    wa = WeatherAnalysis("weather_data.csv")
    wa.main()
         
