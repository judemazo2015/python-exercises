from utils import clear_screen
import inflect
engine = inflect.engine()

def main():
    matrix = [
        [0,  1,  2,  3],
        [4,  5,  0,  7],
        [8,  9, 10, 11],
        [12, 0, 14, 15]
    ]


    get_col_zero(matrix)

def get_col_zero(matrix):
    num_rows = len(matrix)
    num_cols = len(matrix[0])
    cols_zero = []

    for j in range(num_cols):
        for i in range(num_rows):
            if matrix[i][j] == 0:
                cols_zero.append(str(j+1))
                break
    
    print(f"Columns {engine.join(cols_zero)} contain at least one zero")

if __name__ == "__main__":
    main()