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

    if old_val == new_val:
        return  # Nothing to change

    stack = [[sr, sc]]

    while stack:
        r, c = stack.pop()

        if (
            r < 0 or r >= len(matrix) or
            c < 0 or c >= len(matrix[0]) or
            matrix[r][c] != old_val
        ):
            continue

        matrix[r][c] = new_val

        stack.append([r-1, c]) 
        stack.append([r+1, c]) 
        stack.append([r, c-1]) 
        stack.append([r, c+1]) 

    for row in matrix:
        print(row)

if __name__ == "__main__":
    main()
