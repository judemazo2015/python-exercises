from utils import clear_screen

def main():
    width = 6
    length = 8 

    clear_screen()
    make_border(width,length)

def make_border(w, l):
    matrix = [[0]*l for _ in range(w)]

    for i in range(w):
        for j in range(l):
            if i == 0:
                matrix[i][j] = 1
            elif j == 0 or j == l-1:
                matrix[i][j] = 1
            elif i == w-1:
                matrix[i][j] = 1
    
    for row in matrix:
        print(row)

if __name__=="__main__":
    main()