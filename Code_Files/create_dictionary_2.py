class CreateDictionary:
    
    def __init__(self):
        self.keyList = []
        self.valueList = []
        self._dict = {}  # Use _dict to make it a private attribute
        
    def createList(self, keyList, valueList):
        # Ensures the lists are of equal length
        if len(keyList) != len(valueList):
            print("Error: Key list and value list must be of the same length!")
            return
        
        self.keyList = keyList
        self.valueList = valueList
    
    def createDictionary(self):
        # Create dictionary by zipping keyList and valueList together
        self._dict = dict(zip(self.keyList, self.valueList))
        
    def displayDictionary(self):
        # Method to print dictionary in a readable format
        if not self._dict:
            print("Dictionary is empty!")
        else:
            for key, value in self._dict.items():
                print(f"{key} : {value}")
                
    def main(self):
        keyList = ["Frau", "Herr", "Sir", "Madam"]
        valueList = ["Müller", "Mustermann", "Brown", "Allan"]
        
        # Call methods to create and display dictionary
        self.createList(keyList, valueList)
        self.createDictionary()
        self.displayDictionary()

# Check if the script is being run directly
if __name__ == "__main__":
    cd = CreateDictionary()
    cd.main()
