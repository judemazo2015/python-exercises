from utils import clear_screen

def main():
    matrix = [
        [ 1,  2,  3,  4,  5],
        [ 6,  7,  8,  9, 10],
        [11, 12, 13, 14, 15],
        [16, 17, 18, 19, 20]
    ]
    clear_screen()
    get_spiral(matrix)

def get_spiral(matrix):
    n = len(matrix)
    m = len(matrix[0])
    numbers = []
    loops = (min(m, n) + 1) // 2
    down=0
    left=0

    for loop in range(loops):
        append_done=False
        left_col=[]
        for i in range(down,n-down):
            for j in range(left,m-left):
                if i==down:
                    numbers.append(matrix[i][j])
                elif i==n-1-down:
                    numbers.append(matrix[i][-1-j])
                elif j==m-1-left:
                    numbers.append(matrix[i][j])
                elif j==left:
                    left_col.append(matrix[i][j])
        append_done=True

        if append_done and loop!=loops-1:
            for num in left_col:
                numbers.append(num)
        down+=1
        left+=1
    
    print(numbers)

if __name__ == "__main__":
    main()