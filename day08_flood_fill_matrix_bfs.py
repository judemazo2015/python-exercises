from utils import clear_screen

def main():
    matrix = [
        [0, 0, 1, 1],
        [0, 1, 1, 0],
        [1, 1, 0, 0],
        [0, 0, 1, 1]
    ]
    clear_screen()
    flood_fill(matrix)
    print()

def flood_fill(matrix):
    sr = 1
    sc = 2

    old_val = matrix[sr][sc]
    new_val = 2
    matrix[sr][sc] = new_val

    cells = [[sr, sc]]
    
    m=0
    while m < len(cells):

        for i in range(len(matrix)):
            for j in range (len(matrix[0])):
                if check_adjacent_cells(cells[m][0],cells[m][1],i,j):
                    if matrix[i][j] == old_val:
                        matrix[i][j] = new_val
                        cells.append([i, j])                
        m+=1

    for row in matrix:
        print(row)

def check_adjacent_cells(sr, sc, row, col):
    if (
        row == sr and col == sc-1 or
        row == sr and col == sc+1 or
        row == sr-1 and col == sc or
        row == sr+1 and col == sc
    ):
        return True
if __name__ == "__main__":
    main()