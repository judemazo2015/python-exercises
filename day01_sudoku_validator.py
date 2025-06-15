from utils import clear_screen

def main():
    valid_4x4_board = [
    [1, 2, 3, 4],
    [3, 4, 1, 2],
    [2, 1, 4, 3],
    [4, 3, 2, 1]
    ]
    clear_screen()
    print(is_valid_sudoku(valid_4x4_board))

def is_valid_sudoku(sudoku):
    if is_valid_row(sudoku) and is_valid_column(sudoku) and is_valid_subgrid(sudoku):
        return "Valid Sudoku!"
    else:
        return "Invalid Sudoku."

def is_valid_row(sudoku):
    for row in sudoku:
        if len(set(row))!=len(row):
            return False       
    return True

def is_valid_column(sudoku):
    i=0
    column=[]
    all_column=[]
    while i<len(sudoku):
        for line in sudoku:
            column.append(line[i])
        all_column.append(column)
        column = []
        i+=1
    
    for line in all_column:
        for num in line:
            if line.count(num)>1:
                return False
    return True

def is_valid_subgrid(sudoku):
    size = len(sudoku)
    subgrid_size = int(size ** 0.5)

    for row in range(0, size, subgrid_size):
        for col in range(0, size, subgrid_size):
            block = []
            for r in range(row, row + subgrid_size):
                for c in range(col, col + subgrid_size):
                    block.append(sudoku[r][c])
            for num in block:
                if block.count(num) > 1:
                    return False
    return True
                   
if __name__ == "__main__":
    main()