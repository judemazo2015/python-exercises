from utils import clear_screen

def main():

    width = 5
    length = 5

    clear_screen()
    create_diagonal(width, length)

def create_diagonal(w, l):

    matrix = [[0]*l for _ in range(w)]
    
    for i in range(w):
        for j in range(l):
            if j == i or j == (l-1)-i:
                matrix[i][j] = 1
    
    for row in matrix:
        print(row)
if __name__ == "__main__":
    main()