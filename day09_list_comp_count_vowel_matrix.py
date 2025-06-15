matrix = [
    ["alone",  "echo",   "eerie"],
    ["input",  "audio",  "area"],
    ["usage",  "gamma",  "orbit"]
]
row_size, col_size = len(matrix), len(matrix[0])
vowels = 'aeiouAEIOU'

vowel_scores = [
    (matrix[i][j].upper(), vowel_size)
    for i in range(row_size) for j in range(col_size)
    if (j==i or j==row_size-1-i) and
    (vowel_size := sum((2 if matrix[i][j][k-1] == matrix[i][j][k] else 1  for k in range(len(matrix[i][j])) if matrix[i][j][k] in vowels)))>=3 
    ]

print(vowel_scores)

"""
You're given a matrix (2D list of lowercase words).

Create a single list comprehension to produce a list named vowel_scores, following these rules:

Scope – Only consider the main and anti-diagonals, same as before.

Scoring Rule – For each diagonal word, calculate its vowel score:

Each vowel (a, e, i, o, u) counts as 1 point.

Double vowels (aa, ee, ii, oo, uu) in a row count as 2 extra points (so 'look' gives 2 for oo instead of 1).

Filter – Only include diagonal words with vowel scores ≥ 3.

Output – Each element should be a tuple
"""