matrix = [
    [  1,  2,  3,  4,  5,  6,  7,  8,  9],
    [ 32, 33, 34, 35, 36, 37, 38, 39, 10],
    [ 31, 56, 57, 58, 59, 60, 61, 40, 11],
    [ 30, 55, 72, 73, 74, 75, 62, 41, 12],
    [ 29, 54, 71, 80, 81, 76, 63, 42, 13],
    [ 28, 53, 70, 79, 78, 77, 64, 43, 14],
    [ 27, 52, 69, 68, 67, 66, 65, 44, 15],
    [ 26, 51, 50, 49, 48, 47, 46, 45, 16],
    [ 25, 24, 23, 22, 21, 20, 19, 18, 17]
]

row = len(matrix)
col = len(matrix[0])

top, bottom = 0, row
left, right = 0, col

words_in_spiral = []
while top<=bottom and left<=right:
    
    for j in range(left,right):
        words_in_spiral.append(matrix[top][j])

    for i in range(top+1,bottom):
        words_in_spiral.append(matrix[i][right-1])

    for j in range(right-2, left-1, -1):
        words_in_spiral.append(matrix[bottom-1][j])

    for i in range(bottom-2,top,-1):
        words_in_spiral.append(matrix[i][left])

    top, bottom = top+2, bottom-2
    left, right = left+2, right-2


print(words_in_spiral)