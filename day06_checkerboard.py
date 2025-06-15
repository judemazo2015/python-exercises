from utils import clear_screen

def main():
    width = 6
    length = 6
    clear_screen()
    create_checker(width, length)

def create_checker(w, l):
    board = [[0]*l for _ in range(w)]

    for i in range(w):
        for j in range(l):
            if i % 2 == 1 and j % 2 == 1:
                board[i][j] = 1
            elif i %2 == 0 and j % 2 == 0:
                board[i][j] = 1
    
    for row in board:
        print(row)

if __name__=="__main__":
    main()