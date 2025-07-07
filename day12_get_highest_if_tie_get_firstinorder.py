matrix = [
    ["cat", "bat", "cat", "dog"],
    ["bat", "bat", "dog", "dog"],
    ["cat", "bat", "dog", "bat"],
    ["bat", "bat", "cat", "dog"]
]

most_appearance = []
for col in zip(*matrix):
    words=[]
    for word in col:
        words.append((word,col.count(word)))
    most_appearance.append(max(words, key=lambda x:(x[1],sum(-ord(x[0][i]) for i in range(len(x[0])))))[0])

print(most_appearance)

