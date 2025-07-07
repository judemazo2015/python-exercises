def count_connected(matrix, visited, row, col, value):
    if row < 0 or col < 0 or row >= len(matrix) or col >= len(matrix[0]):
        return 0
    if matrix[row][col] == value and (row,col) not in visited:
        visited.append((row,col))
        return (
            1 +
            count_connected(matrix, visited, row -1, col, value) +
            count_connected(matrix, visited, row +1, col, value) +
            count_connected(matrix, visited, row, col + 1, value) +
            count_connected(matrix, visited, row, col -1, value)
        )
    else:
        return 0


matrix = [
  [1, 1, 0],
  [0, 1, 0],
  [1, 0, 1]
]
r, c = 0, 0
r2, c2, = 2, 2
r3, c3 = 0, 1
r4, c4 = 2, 0

print(count_connected(matrix, [], r, c, matrix[r][c]))
print(count_connected(matrix, [], r2, c2, matrix[r2][c2]))
print(count_connected(matrix, [], r3, c3, matrix[r3][c3]))
print(count_connected(matrix, [], r4, c4, matrix[r4][c4]))