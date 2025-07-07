def sum_matrix(matrix, visited, row, col):
    if row < 0 or col < 0 or row >= len(matrix) or col >=len(matrix[0]):
        return 0
    
    if (row, col) not in visited:
        visited.append((row,col))
        total = matrix[row][col] + sum_matrix(matrix, visited, row+1, col) + sum_matrix(matrix, visited, row, col+1)
        return total
    else:
        return 0 

matrix = [
        [1, 2],
        [3, 4]
        ]

print(sum_matrix(matrix,[], 0, 0))