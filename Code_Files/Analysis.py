import logging

class WMetrics:
    def __init__(self, file_name):
        self.file = file_name
        self.data = []
        self.lines = []
        
    def read_csv(self):
        try:
            with open(self.file, "r") as file:
                self.lines = file.readlines()
        except FileNotFoundError:
            logging.error(f"The file: {self.file} could not be found")
            raise SystemExit("Terminating program due to missing file.")
    
    def parse_csv(self):
        if not self.lines:
            logging.error("No lines to parse")
            return
        try:    
            for line in self.lines[1:]:
                parts = line.strip().split(",")
                try:
                    if len(parts) == 3:
                        date, temperature, humidity = parts
                        self.data.append(
                            {
                                "date": date,
                                "temperature": float(temperature),
                                "humidity": float(humidity)
                            }         
                        )
                except ValueError:
                    logging.error("The list length is invalid")
        except Exception as e:
            logging.error(f"Parsing failed: {e}")
    
    def get_max_temp(self):
        if not self.data:
            logging.error("No data to calculate max temperature")
            return
        max_entry = max(self.data, key=lambda x: x["temperature"])
        max_date, max_temperature = max_entry["date"], max_entry["temperature"]
        print(f"Maximum temperature reached on {max_date} with {max_temperature:.2f} °C")
        
    def get_min_temp(self):
        if not self.data:
            logging.error("No data to calculate min temperature")
            return
        min_entry = min(self.data, key=lambda x: x["temperature"])
        min_date, min_temperature = min_entry["date"], min_entry["temperature"]
        print(f"The minimum temperature was reached on {min_date} with {min_temperature:.2f} °C")   
    
    def get_average_temp(self):
        if not self.data:
            logging.error("No data to calculate average temperature")
            return
        total_temp = sum(entry["temperature"] for entry in self.data)
        count = len(self.data)
        average_temp = total_temp / count
        print(f"The average temperature is {average_temp:.2f} °C")
        
    def main(self):
        self.read_csv()
        self.parse_csv()
        self.get_max_temp()
        self.get_min_temp()
        self.get_average_temp()
        
if __name__ == "__main__":
    wm = WMetrics("weather_data.csv")
    wm.main()
            
            