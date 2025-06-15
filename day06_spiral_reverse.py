from utils import clear_screen

def main():

    length  = 5
    width = 3
    clear_screen()
    build_reversed_spiral(width, length)

def build_reversed_spiral(width, length):
    top, bottom = 0, width
    left, right = 0, length

    matrix = [[0]*length for _ in range(width)]
    num = 1

    while top<bottom and left<right:
 
        for j in range(right-1, left-1, -1):
            matrix[top][j] = num
            num+=1
        top+=1

        for i in range(top,bottom):
            matrix[i][left] = num
            num+=1
        left+=1

        if top<bottom:
            for j in range(left,right):
                matrix[bottom-1][j] = num
                num+=1
            bottom-=1

        if left<right:
            for i in range(bottom-1, top-1, -1):
                matrix[i][right-1] = num
                num+=1
            right-=1
    
    for row in matrix:
        print(row)

if __name__ == "__main__":
    main()