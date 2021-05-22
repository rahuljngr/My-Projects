import json
from difflib import get_close_matches

data = json.load(open("/home/rahul/python3/teaching section13/data.json"))

def translate(w):
    w = w.lower()
    if w in data :
        return data[w]
    elif len(get_close_matches(w, data.keys())) >0:
        return "Did you mean %s instead ?" % get_close_matches(w, data.keys())[0]
    else :
        return "The word doesn't exist. Please Double chack it"


word = input("Enter word :")

print(translate(word))