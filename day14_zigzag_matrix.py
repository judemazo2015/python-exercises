matrix = [
    ["ant",   "bee",   "cat",   "dog"],
    ["elk",   "frog",  "goat",  "hare"],
    ["ibex",  "jaguar","koala", "lemur"],
    ["mole",  "newt",  "owl",   "puma"]
]

size = len(matrix)
zigzag_words = []

limit1=0
while limit1<=size:
    for i in range(limit1):
        for j in range(limit1):
            if j == limit1-1-i and limit1%2==0:
                zigzag_words.append(matrix[i][j])
            elif j==limit1-1-i and limit1%2!=0:
                zigzag_words.append(matrix[j][i])
    limit1+=1

print()
limit2 = 0
while limit2<size:
    for k in range(size):
        for l in range(size-1,-1,-1):
            if l == size-k+limit2 and limit2%2==0:
                zigzag_words.append(matrix[l][k])
            elif l == size-k+limit2 and limit2%2!=0:
                zigzag_words.append(matrix[k][l])
    limit2+=1

print(zigzag_words)