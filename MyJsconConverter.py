import json
import os

class MyJsconConverter:
    def __init__(self, myData):
        self.data = myData
    
        with open('cookiesFile.json', 'w') as f:
            json.dump(self.data, f, indent=4)  # Add indent for readability (optional)