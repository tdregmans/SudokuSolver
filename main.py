""" 
    SudokuSolver
    main.py
    
    Thijs Dregmans (tdregmans)
    Version: 3.2
    Last edited: 2024-02-21
"""

# Constants
SIZE = 9
DEBUG_MODE = True
REGULAR_MODE = False

# Import examples and Solver class
from examples import ExampleSudokus
from sudokuSolver import SudokuSolver

print("                           ▄▄                                                   ▄▄                             ")
print(" ▄█▀▀▀█▄█                ▀███          ▀███                  ▄█▀▀▀█▄█         ▀███                             ")
print("▄██    ▀█                  ██            ██                 ▄██    ▀█           ██                             ")
print("▀███▄   ▀███  ▀███    ▄█▀▀███   ▄██▀██▄  ██  ▄██▀▀███  ▀███ ▀███▄     ▄██▀██▄   ██ ▀██▀   ▀██▀  ▄▄█▀██▀███▄███ ")
print("  ▀█████▄ ██    ██  ▄██    ██  ██▀   ▀██ ██ ▄█     ██    ██   ▀█████▄██▀   ▀██  ██   ██   ▄█   ▄█▀   ██ ██▀ ▀▀ ")
print("▄     ▀██ ██    ██  ███    ██  ██     ██ ██▄██     ██    ██ ▄     ▀████     ██  ██    ██ ▄█    ██▀▀▀▀▀▀ ██     ")
print("██     ██ ██    ██  ▀██    ██  ██▄   ▄██ ██ ▀██▄   ██    ██ ██     ████▄   ▄██  ██     ███     ██▄    ▄ ██     ")
print("█▀█████▀  ▀████▀███▄ ▀████▀███▄ ▀█████▀▄████▄ ██▄▄ ▀████▀███▄▀█████▀  ▀█████▀ ▄████▄    █       ▀█████▀████▄   ")
print("                                                                                                               ")
print("                                                                                                               ")
print("Thijs Dregmans (tdregmans)")
print("Version 3.2")
print("===============================================================================================================")

"""

    There are two ways to use the SudokuSolver:

        1. Solve an example Sudoku.
        2. Enter your own Sudoku to solve.

    Both are typed out below. Uncomment the one you want to use.

    The SudokuSolver has a few advanced features:
        1. It can process Sudoku's with a differnt size than 9. This is an optional parameter that has to be passed to the constructor.
        2. It has a Debug mode. When Debug mode is activated, the SudokuSolver print the sudoku to the screen after each iteration.
        3. The SudokuSolver has a maximum number of iterations. This value default set to 20. You can change this, by passing an integer to the `solve()` method.
           The reason the solver has a maximum number of iterations is because if the solver is passed an invalid Sudoku, it will - in theory - never figure that out.

"""

# Function used by `main.py` to save a custom sudoku to solve with SudokuSolver
def enterCustomSudoku():
    print("Enter in a Sudoku.")
    print("Enter the fields row by row, from left to right.")
    print("If a field is empty, enter nothing i.e. ''")
    
    sudoku = []
    for field in range(SIZE * SIZE):
        i = input("Enter field " + str(field) + ": ")
        if i == "":
            sudoku.append([])
        else:
            sudoku.append([int(i)])
    i = input("Is the correct? (y/n) ")
    if i == 'y':
        return sudoku
    else:
        print("retry")



### Usecase 1

# # Create solver
# solver = SudokuSolver(ExampleSudokus.sudoku1)

# solver.solve()

# # Print found solution
# print("Found solution: ")
# print("===============================================================================================================")
# solver.print()



### Usecase 2

# # Create Sudoku
# sudoku = enterCustomSudoku()

# # Create solver
# solver = SudokuSolver(sudoku)

# solver.solve()

# # # Print found solution
# print("Found solution: ")
# print("===============================================================================================================")
# solver.print()
