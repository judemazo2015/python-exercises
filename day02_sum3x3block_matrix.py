from utils import clear_screen

def main():
    matrix = [
    [1, 2, 0, 3, 4],
    [0, 1, 5, 2, 1],
    [4, 0, 1, 0, 0],
    [2, 3, 2, 1, 4],
    [1, 2, 1, 0, 2]
    ]
    clear_screen()
    for row in matrix:
        print(row)
    print(f"\nHighest possible sum: {get_block_sum(matrix)}")

def get_block_sum(matrix):
    block_size = int(input("\nInput block size to get max sum: "))
    limit = len(matrix)-block_size+1
    all_sums=[]
    for row in range(0,limit):
        for col in range(0,limit):
            total = 0
            for r in range(row,row+block_size):
                for c in range(col,col+block_size):
                    total+=matrix[r][c]
            all_sums.append(total)

    print(f"Possible sums: {', '.join(map(str, all_sums))}")
    return max(all_sums)

if __name__=="__main__":
    main()
