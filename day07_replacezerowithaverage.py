from utils import clear_screen

def main():

    matrix = [
        [0,  2,  4],
        [3,  0,  6],
        [7,  8,  0]
    ]
    clear_screen()
    replace_zero_rowaverage(matrix)

def replace_zero_rowaverage(matrix):
    num_rows =  len(matrix)
    num_cols = len(matrix[0])

    for i in range(num_rows):
        avg = int(sum(matrix[i]) / 2)
        for j in range(num_cols):
            if matrix[i][j] == 0:
                matrix[i][j] = avg
    
    for row in matrix:
        print(row)

if __name__=="__main__":
    main()
