def find_paths_iterative(matrix):
    r_size, c_size = len(matrix), len(matrix[0])
    paths = []
    stack = [((0,0),[(0,0)])]

    while stack:
        (r, c),path = stack.pop()

        if (r,c) == (r_size-1, c_size-1):
            paths.append(path)
            continue

        if c+1<c_size and matrix[r][c+1] == 0:
            stack.append(((r,c+1), path+[(r,c+1)]))
        
        if r+1<r_size and matrix[r+1][c] == 0:
            stack.append(((r+1,c),path+[(r+1,c)]))
        
    return paths        

matrix = [
    [0, 0, 0],
    [0, 1, 0]
]

print(find_paths_iterative(matrix))