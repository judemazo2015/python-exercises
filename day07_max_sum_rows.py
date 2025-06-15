from utils import clear_screen
import inflect
engine = inflect.engine()

def main():
    matrix = [
        [2, 4, 4],  
        [3, 6, 1],  
        [1, 2, 3],   
        [5, 5, 0]   
    ]

    clear_screen()
    get_row_maxvalue(matrix)

def get_row_maxvalue(matrix):
    num_rows = len(matrix)
    num_cols = len(matrix[0])
    sums = []

    for i in range(num_rows):
        total = 0
        for j in range(num_cols):
            total+=matrix[i][j]
        sums.append(total)
    
    rows = []
    max_sum = max(sums)
    for i in range(len(sums)):
        if sums[i] == max_sum:
            rows.append(str(i+1)) 

    print(f"Rows {engine.join(rows)} have the maximum sum: {max_sum}")           

if __name__ == "__main__":
    main()