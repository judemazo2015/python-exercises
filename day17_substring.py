import re

def get_substrings(text):
    words = re.findall(r"\b[a-z]+\b",text)
    substrings = [word for word in words if any(word in w for w in words if w!=word)]
    return list(set(substrings))

print(get_substrings("I saw a catcatcher catch a cat and a catcher."))
