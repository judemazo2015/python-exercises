def count_zero_paths(matrix, r, c, visited):
    if r<0 or c<0 or r>=len(matrix) or c>=len(matrix[0]) or matrix[r][c]!=0:
        return 0 
    if (r,c) == (len(matrix)-1, len(matrix[0])-1):
        return 1
    if (r,c) not in visited:
        visited.append((r,c))
        total = (
            count_zero_paths(matrix, r+1, c, visited) +
            count_zero_paths(matrix, r, c+1, visited) +
            count_zero_paths(matrix, r-1, c, visited) +
            count_zero_paths(matrix, r, c-1, visited)
        )
        visited.pop()
        return total
    else:
        return 0
        
matrix = [
    [0,  0,  0],
    [0, -1,  0],
    [0,  0,  0]
]
print(count_zero_paths(matrix, 0, 1, []))