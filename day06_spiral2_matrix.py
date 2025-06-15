from utils import clear_screen

def main():

    matrix = [
        [1, 2, 3],
        [8, 9, 4],
        [7, 6, 5]
    ]

    matrix1 = [
        [1, 2, 3],
        [10, 11, 4],
        [9, 12, 5],
        [8, 7, 6]
    ]

    matrix2 = [
        [1, 2, 3, 4, 5],
        [14, 15, 16, 17, 6],
        [13, 20, 19, 18, 7],
        [12, 11, 10, 9, 8]
    ]

    matrix3 = [
        [1, 2, 3, 4, 5, 6],
        [22, 23, 24, 25, 26, 7],
        [21, 36, 37, 38, 27, 8],
        [20, 35, 42, 39, 28, 9],
        [19, 34, 41, 40, 29, 10],
        [18, 33, 32, 31, 30, 11],
        [17, 16, 15, 14, 13, 12]
    ]

    matrix4 = [
        [1, 2, 3, 4, 5, 6, 7, 8],
        [30, 31, 32, 33, 34, 35, 36, 9],
        [29, 52, 53, 54, 55, 56, 37, 10],
        [28, 51, 66, 67, 68, 57, 38, 11],
        [27, 50, 65, 72, 69, 58, 39, 12],
        [26, 49, 64, 71, 70, 59, 40, 13],
        [25, 48, 63, 62, 61, 60, 41, 14],
        [24, 47, 46, 45, 44, 43, 42, 15],
        [23, 22, 21, 20, 19, 18, 17, 16]
    ]

    clear_screen()
    show_spiral(get_spiral(matrix))
    show_spiral(get_spiral(matrix1))
    show_spiral(get_spiral(matrix2))
    show_spiral(get_spiral(matrix3))
    show_spiral(get_spiral(matrix4))

def get_spiral(matrix):
    length = len(matrix[0])
    width = len(matrix)
    spiral_loops = (min(width,length)+1)//2
    nums_spiraled = []
    outer = 0

    for _ in range(spiral_loops):
        left_colnums = []
        for i in range(outer, width-outer):
            for j in range(outer, length-outer):

                if i == outer:
                    nums_spiraled.append(matrix[i][j])
                
                elif j == (length-1)-outer and i!=(width-1)-outer:
                    nums_spiraled.append(matrix[i][j])
                
                elif i == (width-1)-outer:
                    nums_spiraled.append(matrix[i][-1-j])
                
                elif j == outer:
                    left_colnums.append(matrix[-1-i][j])
        
        for num in left_colnums:
            nums_spiraled.append(num)     
        outer+=1
    
    return nums_spiraled

def show_spiral(spiral):
    print("\nSpiral numbers: ", end="")
    for num in spiral:
        print(num,end=" ")
    print()

if __name__=="__main__":
    main()