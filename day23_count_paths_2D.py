def count_paths(row, col, m, n):
    if (row,col) == (m-1, n-1):
        return 1    
    if row >= m or col>= n:
        return 0
    return count_paths(row+1, col, m, n) + count_paths(row, col+1, m, n)

print(count_paths(0,0,2,2))