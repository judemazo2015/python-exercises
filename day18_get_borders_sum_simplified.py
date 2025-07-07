def get_borders_sum(matrix):
    rsize = len(matrix)
    return sum([
        sum([num for num in matrix[0]]),
        sum([num for num in matrix[-1]]),
        sum([matrix[i][0] for i in range(1, rsize-1)]),
        sum([matrix[i][-1] for i in range(1, rsize-1)]),
    ])

matrix = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15],
    [16, 17, 18, 19, 20],
    [21, 22, 23, 24, 25]
]

print(get_borders_sum(matrix))