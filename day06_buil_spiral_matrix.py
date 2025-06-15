from utils import clear_screen

def main():
    width = 5
    length = 4
    clear_screen()
    build_spiral_matrix(width, length)

def build_spiral_matrix(w, l):
    matrix = [[0]*l for _ in range(w)]
    spiral_loops = (min(w,l)+1)//2
    top, bottom, left, right = 0, w, 0, l
    num = 1

    while top < bottom and left < right:

        for i in range(left, right):
            matrix[top][i] = num
            num+=1
        top+=1
        
        for j in range(top, bottom):
            matrix[j][right-1] = num
            num+=1
        right-=1

        if top<bottom:
            for i in range(right-1, left-1, -1):
                matrix[bottom-1][i] = num
                num+=1
            bottom-=1

        if left<right:
            for j in range(bottom-1, top-1,-1):
                matrix[j][left] = num
                num+=1
            left+=1

    for row in matrix:
      print(row)

if __name__ == "__main__":
    main()
