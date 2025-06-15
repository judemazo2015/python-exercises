from utils import clear_screen

def main():
    width = 5
    length = 5
    clear_screen()
    create_numframes(width, length)

def create_numframes(w, l):
    matrix = [[0]*l for _ in range(w)]
    top, bottom = 0, w
    left, right = 0, l
    num = 1

    while top<bottom and left<right:
   
        for j in range(left,right):
            matrix[top][j] = num
        top+=1
            
        for i in range(top,bottom):
            for j in range(left,right):
                if j == left or j == right-1:
                    matrix[i][j] = num
        right-=1
        left+=1
        
        if top<bottom:
            for j in range(right-1, left-1,-1):
                matrix[bottom-1][j] = num
            bottom-=1
        num+=1
    
    for row in matrix:
        print(row)

if __name__=="__main__":
    main()