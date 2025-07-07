def count_regions(matrix, vis, r, c):
    counts = 0
    if r == len(matrix):
        return 0
    if c == len(matrix[0]):
        return count_regions(matrix, vis, r+1, 0)
    if matrix[r][c] == 1 and (r,c) not in vis:
        count_connected(matrix, vis, r, c, matrix[r][c])
        counts+=1
        
    return counts + count_regions(matrix, vis, r, c+1)

def count_connected(matrix, visited, row, col, value):
    if row < 0 or col < 0 or row >= len(matrix) or col >= len(matrix[0]):
        return 0
    if matrix[row][col] == value and (row,col) not in visited:
        visited.append((row,col))
        print(visited)
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

print(count_regions(matrix,[], 0, 0))