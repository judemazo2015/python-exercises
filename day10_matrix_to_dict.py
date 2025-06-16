word_counts = {
    'the': 12,
    'cat': 3,
    'sat': 2,
    'on': 5,
    'mat': 2,
    'and': 7,
    'looked': 1,
    'at': 4,
    'me': 1
}

result = {word:count for word,count in word_counts.items() if count>3}

print(result)