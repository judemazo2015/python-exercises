def is_center_biggest(matrix):
    mid, size = len(matrix)//2, len(matrix)
    neighbors = [(mid-1, mid), (mid+1, mid), (mid, mid-1), (mid, mid+1)]
    for i in range(size):
        for j in range(size):
            if (((i==mid+1 or i==mid-1) and (j==mid+1 or j==mid-1)) or
            (i,j in neighbors)) and matrix[i][j] > matrix[mid][mid]:
                return False
    return True

print(is_center_biggest([
        [1, 2, 3],
        [4, 9, 6],
        [7, 8, 5]
        ]
    ))

print(is_center_biggest([
        [5, 1, 5],
        [2, 3, 2],
        [5, 4, 5]
        ]
    ))

print(is_center_biggest([
        [10, 22, 30, 22, 10],
        [21, 25, 28, 25, 21],
        [19, 24, 99, 24, 19],
        [21, 23, 27, 23, 21],
        [10, 22, 30, 22, 10]
        ]
    ))

print(is_center_biggest([
        [10, 22, 30, 22, 10],
        [21, 25, 28, 25, 21],
        [19, 24, 26, 24, 19],
        [21, 23, 27, 23, 21],
        [10, 22, 30, 22, 10]
        ]
    ))