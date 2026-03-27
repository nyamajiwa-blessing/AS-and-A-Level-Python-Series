# Declaration
matrix = [[1,2,3], [4,5,6], [7,8,9]]
print(matrix)

sudoku_grid = [[0 for _ in range(9)] for _ in range(9)]
print(sudoku_grid)

# Printing a list comprehension
for row in sudoku_grid:
    for value in row:
        print(value, end=" ")
    print()

# Using indicies
for i in range(len(sudoku_grid)):
    for j in range(len(sudoku_grid[i])):
        print(f"grid[{i}][{j}] = {sudoku_grid[i][j]}")
        
some_grid = [['X' for _ in range(3)] for _ in range(9)]
for row in some_grid:
    for value in row:
        print(value, end=" ")
    print()