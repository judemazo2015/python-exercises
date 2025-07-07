def count_paths(matrix, tel, vis, r, c):
    if r >= len(matrix) or c >= len(matrix[0]) or matrix[r][c] == 1:
        return 0
    if (r,c) == (len(matrix)-1, len(matrix[0])-1):
        return 1
    if (r,c) not in vis:
        vis.append((r,c))
        if (r,c) in tel:
            nr, nc = tel[(r,c)]
            total = (count_paths(matrix, tel, vis, nr, nc)+
                     count_paths(matrix, tel, vis, r+1, c)+
                count_paths(matrix, tel, vis, r, c+1)
            )
            vis.pop()
            return total
        total = ( count_paths(matrix, tel, vis, r+1, c)+
                count_paths(matrix, tel, vis, r, c+1)
        )
        vis.pop()
        return total
    else:
        return 0
    
matrix = [
    [0, 0, 0],
    [1, 1, 0],
    [0, 0, 0]
]

teleporters = {
    (0, 1): (2, 1)
}
print(count_paths(matrix, teleporters, [], 0, 0))