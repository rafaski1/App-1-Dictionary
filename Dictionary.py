"""
This dictionary app will allow user to enter a word to find out its definition.
JSON file will be used to store and access dictionary data.
logic:
if user enters a correct word that is a part of dictionary, a definition should be returned
if user misspelled a word, a choice should be given to either choose a close enough word or try again
if no word is find in a dictionary an error message should appear
"""

import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def dictionary(w):
    w = w.lower()
    if w in data:
        return data[w]
    elif w.title() in data:
        return data[w.title()]
    elif w.upper() in data:
        return data[w.upper()]
    elif len(get_close_matches(w, data.keys())) > 0:
        yn = input("Did you mean %s instead? If yes press Y, if not press N: ") % get_close_matches(w, data.keys())[0]
        if yn == "Y":
            return data[get_close_matches(w, data.keys())[0]]
        elif yn == "N":
            return "The word doesn't exist. Please double check it."
        else:
            return "We didn't understand your entry."
    else:
        return "The word doesn't exist. Please double check it."

word = input("Enter a word: ")

output = dictionary(word)

if type(output) == list:
    for i in output:
        print(i)
else:
    print(output)




