from utils import clear_screen

def main():
    matrix =[
    [1, 2, 3],
    [4, 5, 6]
    ]
    new_matrix = transpose_matrix(matrix)
    clear_screen()
    show_matrices(matrix,new_matrix)

def transpose_matrix(matrix):
    transposed=[]
    for col in range(len(matrix[0])):
        new_row=[]
        for row in range(len(matrix)):
            new_row.append(matrix[row][col])
        transposed.append(new_row)
    return transposed

def show_matrices(matrix,new_matrix):
    print("Matrix")
    for row in matrix:
        print(row)
    
    print("\nTransposed Matrix")
    for row in new_matrix:
        print(row)

if __name__=="__main__":
    main()