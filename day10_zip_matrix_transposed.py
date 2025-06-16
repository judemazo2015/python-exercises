matrix = [
    [1, 2, 3],
    [4, 5, 6]
]

transposed = []
for i, j in zip(*matrix):
    transposed.append((i,j))

print(transposed)