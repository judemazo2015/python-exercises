def main():
    matrix = [
        [11, 12, 13, 14],
        [15, 16, 17, 18],
        [19, 20, 21, 22],
        [23, 24, 25, 26]
    ]

    show_diagonals((get_diagonals(matrix)))

def get_diagonals(matrix):
    n=len(matrix)
    diagonals=[[0]*n for _ in range(2)]

    x=0
    for i in range(n):
        diagonals[0][i] = matrix[i][x]
        x+=1
    
    x=0
    for i in range(n):
        diagonals[1][i] = matrix[i][-1-x]
        x+=1

    return diagonals

def show_diagonals(diagonals):
    print("\nMain diagonal: ",end="")
    for i in diagonals[0]:
        print(i,end=" + ")
    print(f" = {sum(diagonals[0])}")

    print("Anti-diagonal: ",end="")
    for i in diagonals[1]:
        print(i,end=" + ")
    print(f" = {sum(diagonals[1])}")

main()
