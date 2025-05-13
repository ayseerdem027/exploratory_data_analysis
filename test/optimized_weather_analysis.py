class WeatherAnalysis:
    def __init__(self, file_name):
        self.file_name = file_name
        self.lines = []
        self.data = []

    def read_csv(self):
        """Reads the content of the CSV file into a list of lines."""
        try:
            with open(self.file_name, "r") as file:
                self.lines = file.readlines()
        except FileNotFoundError:
            print(f"Error: The file '{self.file_name}' was not found.")
            self.lines = []

    def parse_csv(self):
        """Parses the CSV lines into structured data (list of dictionaries)."""
        if not self.lines:
            print("No lines to parse.")
            return
        
        self.data = []
        for line in self.lines[1:]:  # Skip header
            parts = line.strip().split(",")
            if len(parts) == 3:
                date, temperature, humidity = parts
                try:
                    self.data.append({
                        "date": date,
                        "temperature": float(temperature),
                        "humidity": float(humidity)
                    })
                except ValueError:
                    print(f"Warning: Skipping invalid data line: {line}")

    def calculate_max_temp(self):
        """Finds and prints the maximum temperature and corresponding date."""
        if not self.data:
            print("No data available to calculate maximum temperature.")
            return
        
        max_entry = max(self.data, key=lambda x: x["temperature"])
        print(f"The maximum temperature was {max_entry['temperature']}°C on {max_entry['date']}.")

    def calculate_min_temp(self):
        """Finds and prints the minimum temperature and corresponding date."""
        if not self.data:
            print("No data available to calculate minimum temperature.")
            return
        
        min_entry = min(self.data, key=lambda x: x["temperature"])
        print(f"The minimum temperature was {min_entry['temperature']}°C on {min_entry['date']}.")

    def calculate_average_temp(self):
        """Calculates and prints the average temperature."""
        if not self.data:
            print("No data available to calculate average temperature.")
            return
        
        total_temp = sum(entry["temperature"] for entry in self.data)
        average_temp = total_temp / len(self.data)
        print(f"The average temperature is {average_temp:.2f}°C.")

    def main(self):
        """Main function to orchestrate the weather analysis."""
        self.read_csv()
        self.parse_csv()
        self.calculate_max_temp()
        self.calculate_min_temp()
        self.calculate_average_temp()

if __name__ == "__main__":
    wa = WeatherAnalysis("weather_data.csv")
    wa.main()
