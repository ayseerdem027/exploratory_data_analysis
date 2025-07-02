class CreateDictionary:
    
    def __init__(self):
        self.keyList = []
        self.valueList = []
        self.dictionary = {}
    
    def createList(self, keyList, valueList):
        if len(keyList) != len(valueList):
            print("Error: The length of the lists have to be the same")
        
        self.keyList = keyList
        self.valueList = valueList
            
    def createDictionary(self):
        try:
            self.dictionary = dict(zip(self.keyList, self.valueList))
        except Exception as e:
            print(f"Error creating dictionary: {e}")
        
    def displayDictionary(self):
        if not self.dictionary:
            print("The Dictionary is empty")
        else:
            for key, value in self.dictionary.items():
                print(f"{key} {value}")
    
    def main(self):
        keyList = ["Frau", "Herr", "Sir", "Madam"]
        valueList = ["Müller", "Mustermann", "Brown", "Allan"]
        self.createList(keyList, valueList)
        self.createDictionary()
        self.displayDictionary()
        
if __name__ == "__main__":
    cd = CreateDictionary()
    cd.main()    
    