from utils import clear_screen

def main():
    matrix = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        [13, 14, 15, 16]
    ]
    clear_screen()
    for row in matrix:
        print(row)
    rotate(get_rotation(),matrix)

def get_rotation():
    rotate = input(
        "\nChoose the rotation you prefer from the options below. Type:\n"
        "A -> 90° Clockwise\n"
        "B -> 90° Counterclockwise\n"
        "C -> - 180°\n"
    ).strip().lower()
    return rotate

def rotate(option,matrix):
    if option == 'a':
        transpose(matrix)
        swap_row(matrix)
    elif option == 'b':
        transpose(matrix)
        swap_column(matrix)
    elif option == 'c':
        swap_row(matrix)
        swap_column(matrix)
    elif option == 'x':
        return
    else:
        print("Invalid option.")
    
    clear_screen()
    for row in matrix:
        print(row)
    print()

def transpose(matrix):
    n = len(matrix)
    for i in range(n):
        for j in range(i+1,n):
            matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j]

def swap_row(matrix):
    n =len(matrix)
    for i in range(n):
        for j in range(n//2):
            matrix[i][j], matrix[i][-1-j] = matrix[i][-1-j],matrix[i][j]

def swap_column(matrix):
    n = len(matrix)
    for i in range(n):
        for j in range(n//2):
            matrix[j][i], matrix[-1-j][i] = matrix[-1-j][i], matrix[j][i]

if __name__=="__main__":
    main()
