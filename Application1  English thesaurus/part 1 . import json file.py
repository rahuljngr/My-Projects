import json

data = json.load(open("/home/rahul/python3/teaching section13/data.json"))

def translate(w):
    return data[w]


word = input("Enter word :")

print(translate(word))