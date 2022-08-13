import numpy as np

grid = []

 # to keep track of the row entered by the user
row_num = 1
 
# loop to input the sudoku data row wise from the user
while True:
    print_statement = f'Enter Row {row_num}:'
    row = list(input(print_statement)) #takes input from the user
    row_num += 1
    inputs = []

    # splits the data into 9 numbers and converts it into a number list
    for n in row:
        inputs.append(int(n))
    grid.append(inputs)

    if len(grid) == 9:
        break
    print('Row ' + str(len(grid)) + ' Complete')

# SOLVES THE SUDOKU PUZZLE
def possible(x, y, n):
    # Checks if the number is present across the row
    for i in range(0, 9):
        if grid[i][x] == n and i != y: 
            return False

    # Checks if the number is present across the column
    for i in range(0, 9):
        if grid[y][i] == n and i != x:
            return False

    # Checks if the number in the small 3 x 3 grid
    x_square = (x // 3) * 3
    y_square = (y // 3) * 3
    for X in range(x_square, x_square + 3):
        for Y in range(y_square, y_square + 3):  
            if grid[Y][X] == n:
                return False    
    return True

def solve():
    global grid
    for y in range(9):
        for x in range(9):
            if grid[y][x] == 0:
                for n in range(1, 10):
                    if possible(x, y, n):
                        grid[y][x] = n
                        solve()
                        grid[y][x] = 0
                return

    # prints the solved sudoku grid
    print()
    print("Solved sudoku puzzle:")
    print(np.matrix(grid)) 

solve()