from utils import clear_screen

def main():
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    new_matrix=rotate_matrix(matrix)
    clear_screen()
    show_matrices(matrix,new_matrix)

def rotate_matrix(matrix):
    rotated=[]
    for col in range(len(matrix[0])):
        new_row=[]
        for row in range(len(matrix) -1, -1, -1):
            new_row.append(matrix[row][col])
        rotated.append(new_row)
    return rotated

def show_matrices(matrix,new_matrix):
    print("Matrix:\n")
    for row in matrix:
        print(row)
    
    print("\nRotated Matrix(90° Clockwise):\n")
    for row in new_matrix:
        print(row)
    print()

if __name__=="__main__":
    main()