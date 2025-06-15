from utils import clear_screen

def main():
    matrix = [
        [1,  2,  3,  4,  5],
        [6,  7,  8,  9, 10],
        [11, 12, 13, 14, 15],
        [16, 17, 18, 19, 20],
        [21, 22, 23, 24, 25]
    ]

    matrix1 = [
        [1,  2,  3],
        [4,  5,  6],
        [7,  8,  9],
        [10, 11, 12]
    ]


    clear_screen()
    get_border_nums(matrix)   
    get_border_nums(matrix1) 

def get_border_nums(matrix):
    width = len(matrix)
    length = len(matrix[0])
    border_nums = []
    top, bottom = 0, width
    right = length

    for j in range(length):
       border_nums.append(matrix[0][j])
    top+=1
    
    if top<bottom:
        for i in range(top,width):
            border_nums.append(matrix[i][right-1])
        right-=1
    
    if right>1:
        for j in range(right-1, -1, -1):
            border_nums.append(matrix[bottom-1][j])
        bottom-=1
    
    if top<bottom:
        for i in range(bottom-1, top-1, -1):
            border_nums.append(matrix[i][0])
    
    print("Border numbers: ", end='')
    for num in border_nums:
        print(num,end=' ')
    print()

if __name__ == "__main__":
    main()
