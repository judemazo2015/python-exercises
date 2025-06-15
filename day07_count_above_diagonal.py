from utils import clear_screen

def main():
    matrix = [
        [1,  2,  3,  4],
        [5,  6,  7,  8],
        [9, 10, 11, 12],
        [13,14, 15, 16]
    ]
    clear_screen()
    count_above_main(matrix)

def count_above_main(matrix):

    size = len(matrix)
    count = 0

    for i in range(size):
        for j in range(size):
            if j>i:
                count+=1
    
    print(f"There are {count} numbers above the main diagonal\n")

if __name__=="__main__":
    main()