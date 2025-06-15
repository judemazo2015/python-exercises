from utils import clear_screen

def main():
    matrix = [
        [ 2,  4,  5,  6],
        [ 7,  8,  9, 10],
        [11, 12, 13, 14],
        [15, 16, 17, 18]
    ]

    clear_screen()
    count_prime(matrix)

def count_prime(matrix):

    row_size = len(matrix)
    col_size = len(matrix[0])
    count = 0

    for i in range(row_size):
        for j in range(col_size):
            if is_prime(matrix[i][j]):
                count+=1
    print(f"There are {count} prime numbers in the matrix.")


def is_prime(num):    
    if num<=1:
        return False

    for i in range(2,int(num**0.5)+1):
        if num % i == 0:
            return False
    return True

if __name__=="__main__":
    main()