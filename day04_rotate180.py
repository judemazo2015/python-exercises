from utils import clear_screen

def main():
    matrix = [
    [11, 12, 13, 14],
    [15, 16, 17, 18],
    [19, 20, 21, 22],
    [23, 24, 25, 26]
    ]   
    clear_screen()
    show_matrix(rotate_matrix(matrix))
    print()

def rotate_matrix(matrix):
    n = len(matrix)

    for i in range(n):
        for j in range(n//2):
            matrix[i][j], matrix[i][-1-j] = matrix[i][-1-j], matrix[i][j]
    
    for i in range(n//2):
        for j in range(n):
            matrix[i][j], matrix[-1-i][j] = matrix[-1-i][j], matrix[i][j]

    return matrix
   
def show_matrix(matrix):
    for row in matrix:
        for i in row:
            print(i,end=" ")
        print()

if __name__ == "__main__":
    main()