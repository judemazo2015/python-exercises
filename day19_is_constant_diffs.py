def consistent_rows(matrix):
    return [row for row in matrix if all(row[j+1]-row[j] == row[1]-row[0] for j in range(len(row)-1))]

print(consistent_rows([
        [2, 4, 6, 8],     #constant diff = 2
        [1, 3, 5, 9],     #NOT constant diff 
        [10, 20, 30, 40], #constant diff = 10
        [7, 7, 7, 7]      #constant diff = 0
        ]
    ))