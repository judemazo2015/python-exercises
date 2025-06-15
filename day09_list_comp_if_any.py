matrix = [
    ["plant", "echo",   "oval"],
    ["drum",  "area",   "kite"],
    ["use",   "gym",    "bold"]
]
row_size, col_size = len(matrix), len(matrix[0])
vowels = 'aeiouAEIOU'

results =  [
    matrix[i][j][::-1].title() for i in range(row_size) for j in range(col_size)
    if (j == i or j==(row_size-1)-i) and
    any(matrix[i][j][k] in vowels and matrix[i][j][k-1] not in vowels and matrix[i][j][k+1] not in vowels for k in range(1,len(matrix[i][j])-1))
    ] 

print(results)