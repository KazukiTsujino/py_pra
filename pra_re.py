import re

text = "The ghost that says boo haunts the loo."

def regular_extension(mess):
    words = re.findall(".oo",mess)
    for word in words:
        print(word)

regular_extension(text)