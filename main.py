""" 
    SudokuSolver
    main.py
    
    Thijs Dregmans (tdregmans)
    Version: 3.1
    Last edited algorithm: 2023-07-27
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
print("Version 3.1")
print("===============================================================================================================")

# Create solver

solver = SudokuSolver(ExampleSudokus.sudoku1)
solver.solve()
print("Found solution: ")
print("===============================================================================================================")
solver.print()
print("===============================================================================================================")

# def enterSudoku():
#     print("Enter in a sudoku.")
#     print("Enter the fields row by row, from left to right.")
#     print("If a field is empty, enter nothing i.e. ''")
    
#     sudoku = []
#     printSudoku()
#     for field in range(SIZE * SIZE):
#         i = input("Enter field " + str(field) + ": ")
#         if i == "":
#             sudoku.append([])
#         else:
#             sudoku.append([int(i)])
#     printSudoku()
#     i = input("Is the correct? (y/n) ")
#     if i == 'y':
#         return
#     else:
#         print("retry")
#         enterSudoku()