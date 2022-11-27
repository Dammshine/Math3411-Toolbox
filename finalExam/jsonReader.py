import json

class Dictionary():
    dictionary = {}

    def __init__(self):
        # Opening JSON file
        f = open('words_dictionary.json')
        data = json.load(f)
        for i in data:
            self.dictionary[i] = True
    
    def search(self, s : str):
        if s in self.dictionary:
            return True
        return False