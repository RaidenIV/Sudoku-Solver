def is_valid_move(grid, row, col, number):
    # Check if 'number' is already in the current row
    for x in range(9):
        if grid[row][x] == number:
            return False
    
    # Check if 'number' is already in the current column
    for x in range(9):
        if grid[x][col] == number:
            return False

    # Determine the starting row and column of the 3x3 subgrid containing (row, col)
    corner_row = row - row % 3
    corner_col = col - col % 3
    
    # Check if 'number' is already in the 3x3 subgrid
    for x in range(3):
        for y in range(3):
            if grid[corner_row + x][corner_col + y] == number:
                return False

    # If 'number' is not already in the row, column, or subgrid, it's a valid move
    return True

def solve(grid, row, col):
    # Base case: If col reaches 9 (end of the row), move to the next row
    if col == 9:
        if row == 8:
            return True
        row += 1
        col = 0

    # If the cell is already filled, move to the next column
    if grid[row][col] > 0:
        return solve(grid, row, col + 1)

    # Try placing numbers from 1 to 9 in the current cell
    for num in range(1, 10):
        if is_valid_move(grid, row, col, num):
            grid[row][col] = num

            # Recursively attempt to solve the puzzle for the next column
            if solve(grid, row, col + 1):
                return True

        # Backtrack if the current number doesn't lead to a solution
        grid[row][col] = 0

    # If no number leads to a solution, return False
    return False

# Sudoku grid to be solved
grid = [[0, 0, 0, 0, 0, 0, 6, 8, 0],
        [0, 0, 0, 0, 7, 3, 0, 0, 9],
        [3, 0, 9, 0, 0, 0, 0, 4, 5],
        [4, 9, 0, 0, 0, 0, 0, 0, 0],
        [8, 0, 3, 0, 5, 0, 9, 0, 2],
        [0, 0, 0, 0, 0, 0, 0, 3, 6],
        [9, 6, 0, 0, 0, 0, 3, 0, 8],
        [7, 0, 0, 6, 8, 0, 0, 0, 0],
        [0, 2, 8, 0, 0, 0, 0, 0, 0]]

# Attempt to solve the Sudoku puzzle
if solve(grid, 0, 0):
    # Print the solved grid
    for i in range(9):
        for j in range(9):
            print(grid[i][j], end=" ")
        print()
else:
    print("No Solution For This Sudoku")
