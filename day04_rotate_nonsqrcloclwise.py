from utils import clear_screen

def main():
    matrix = [
        [1,  2,  3,  4,  5],
        [6,  7,  8,  9, 10],
        [11, 12, 13, 14, 15]
    ]
    clear_screen()
    show_matrix(rotate_matrix(matrix))

def rotate_matrix(matrix):
    n =  len(matrix[0])
    m = len(matrix)
    new_matrix = [[0]*m for _ in range(n)]

    for i in range(n):
        for j in range(m):
            new_matrix[i][j] = matrix[-1-j][i]

    return new_matrix

def show_matrix(matrix):
    for row in matrix:
        for i in row:
            print(f"{i:<4}",end="")
        print()
    print()

if __name__ == "__main__":
    main()