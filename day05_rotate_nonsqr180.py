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
    n = len(matrix)
    m = len(matrix[0])

    for i in range(n):
        for j in range(m//2):
            matrix[i][j], matrix[i][-1-j]=matrix[i][-1-j],matrix[i][j]
    
    for i in range(n//2):
        matrix[i],matrix[-1-i]=matrix[-1-i],matrix[i]
    
    return matrix

def show_matrix(matrix):
    print()
    for row in matrix:
        for i in row:
            print(f"{i:<4}",end="")
        print()
    print()

if __name__=="__main__":
    main()