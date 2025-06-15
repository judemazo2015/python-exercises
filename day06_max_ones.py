from utils import clear_screen
import random

def main():

    width = 5
    length = 5
    clear_screen()
    generate_max_ones(width, length)

def generate_max_ones(w,l):

    matrix = [[0]*l for _ in range(w)]

    removed_col = []

    for row in matrix:
        for _ in range(l):
            col =  random.randint(0, l-1)

            if col not in removed_col:            
                row[col] = 1
                removed_col.append(col)
                break
    
    for row in matrix:
        print(row)
        
if __name__=="__main__":
    main()