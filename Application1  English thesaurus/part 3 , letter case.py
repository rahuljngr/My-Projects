import json

data = json.load(open("/home/rahul/python3/teaching section13/data.json"))

def translate(w):
    w = w.lower()
    if w in data :
        return data[w]
    else :
        return "The word doesn't exist. Please Double chack it"


word = input("Enter word :")

print(translate(word))