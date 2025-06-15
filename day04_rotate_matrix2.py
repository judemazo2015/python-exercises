from utils import clear_screen

def main():
    matrix = [
        [1, 2, 3],  
        [4, 5, 6],
        [7, 8, 9]
    ]
    show_matrix(rotate_matrix(matrix))

def rotate_matrix(matrix):    
    for i in range(len(matrix)): 
        for j in range(i+1,len(matrix)):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    
    for row in matrix:
        for i in range(len(row)//2):
            row[i],row[-1-i]=row[-1-i],row[i]
    
    return matrix

def show_matrix(matrix):
    for row in matrix:
        print(row)
        
if __name__=="__main__":
    main()
