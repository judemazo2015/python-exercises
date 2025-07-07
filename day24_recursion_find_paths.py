def find_paths(matrix, r, c, path, all_paths):
    if r >= len(matrix) or c >= len(matrix[0]) or matrix[r][c] == 1: 
        return
    path.append((r,c))
    if (r,c) == (len(matrix)-1, len(matrix[0])-1):
        all_paths.append(path[:])
    find_paths(matrix, r+1, c, path, all_paths)
    find_paths(matrix, r, c+1, path, all_paths)
    path.pop()
    return all_paths
    

matrix = [
    [0, 0, 0],
    [0, 1, 0]
]
all_paths = []
find_paths(matrix, 0,0, [], all_paths)
print(all_paths)
