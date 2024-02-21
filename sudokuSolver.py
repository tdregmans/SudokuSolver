""" 
    SudokuSolver
    SudokuSolver.py
    
    Thijs Dregmans (tdregmans)
    Version: 3.1
    Last edited algorithm: 2023-07-27
    Last edited: 2024-02-21
"""

# Constants
SIZE = 9
DEBUG_MODE = True
REGULAR_MODE = False

class SudokuSolver:
    """
        Solves the Sudoku
    """
    def __init__(self, sudoku, size = SIZE, mode = REGULAR_MODE):
        self.sudoku = sudoku
        self.size = size
        self.mode = mode

        # initialize Sudoku to solve
        for x in range(self.size ** 2):
            if len(self.sudoku[x]) == 0:
                self.sudoku[x] = (list(range(1, self.size + 1)))

    def print(self):
        """
            Print the Sudoku with the current known fields
        """
        for x in range(self.size ** 2):
            if len(self.sudoku[x]) == 1:
                print(str(self.sudoku[x][0]) + "   ", end='')
            else:
                print("x   ", end='')
            if x % 9 == 8:
                print()

    def isSolved(self):
        """
            Returns True, if Sudoku is solved; else return False
        """
        for x in range(self.size ** 2):
            if len(self.sudoku[x]) != 1:
                return False
        return True


    def __row(self, location):
        """
            (Private method) Return the id of the row that location is located in
        """
        return location // self.size

    def __col(self, location):
        """
            (Private method) Return the id of the col that location is located in
        """
        return location % self.size

    def __sub(self, location):
        """
            (Private method) Return the id of the subGrid that location is located in
        """
        return (self.__row(location) // 3) * 3 + (self.__col(location) // 3)

    def __rowLocations(self, id):
        """
            (Private method) Return a list with all locations of the row with the specified id
        """
        return list(range(id * self.size, id * self.size + self.size))

    def __colLocations(self, id):
        """
            (Private method) Return a list with all locations of the column with the specified id
        """
        return list(range(id, self.size * self.size, self.size))

    def __subLocations(self, id):
        """
            (Private method) Return a list with all locations of the subgrid with the specified id
        """
        firstFieldInSub = ((id // 3) * 3) * 9 + ((id % 3) * 3)
        return [firstFieldInSub, firstFieldInSub + 1, firstFieldInSub + 2,
                firstFieldInSub + 9, firstFieldInSub + 10, firstFieldInSub + 11,
                firstFieldInSub + 18, firstFieldInSub + 19, firstFieldInSub + 20]

    def __removePossiblityRow(self, location, possibility):
        """
            (Private method) Eliminate the values that are no longer possibilities in row
        """
        for x in self.__rowLocations(self.__row(location)):
            if possibility in self.sudoku[x] and len(self.sudoku[x]) != 1:
                self.sudoku[x].remove(possibility)

    def __removePossiblityCol(self, location, possibility):
        """
            (Private method) Eliminate the values that are no longer possibilities in column
        """
        for x in self.__colLocations(self.__col(location)):
            if possibility in self.sudoku[x] and len(self.sudoku[x]) != 1:
                self.sudoku[x].remove(possibility)

    def __removePossiblitySub(self, location, possibility):
        """
            (Private method) Eliminate the values that are no longer possibilities in subgrid
        """
        for x in self.__subLocations(self.__sub(location)):
            if possibility in self.sudoku[x] and len(self.sudoku[x]) != 1:
                self.sudoku[x].remove(possibility)
                

    def __removePossiblity(self, location, possibility):
        """
            (Private method) Eliminate the values that are no longer possibilities in the rows, columns
        """
        self.__removePossiblityRow(location, possibility)
        self.__removePossiblityCol(location, possibility)
        self.__removePossiblitySub(location, possibility)

    def __assignInRow(self, location, possibility):
        """
            (Private method) Assign the possibility to the only location in the row
        """
        for x in self.__rowLocations(self.__row(location)):
            if possibility in self.sudoku[location] and len(self.sudoku[x]) != 1:
                self.sudoku[x] = [possibility]
                return
            
    def __assignInCol(self, location, possibility):
        """
            (Private method) Assign the possibility to the only location in the column
        """
        for x in self.__colLocations(self.__col(location)):
            if possibility in self.sudoku[location] and len(self.sudoku[x]) != 1:
                self.sudoku[x] = [possibility]
                return
            
    def __assignInSub(self, location, possibility):
        """
            (Private method) Assign the possibility to the only location in the subgrid
        """
        for x in self.__subLocations(self.__sub(location)):
            if possibility in self.sudoku[location] and len(self.sudoku[x]) != 1:
                self.sudoku[x] = [possibility]
                return

    def __assignRow(self, location):
        """
            (Private method) Assign all possibilities to the location in all rows
        """
        sumRow = []
        for x in self.__rowLocations(self.__row(location)):
            if len(self.sudoku[x]) != 1:
                sumRow.extend(self.sudoku[x])
        sumRow.sort()
        for x, count in list(set(map(lambda x:(x, sumRow.count(x)), sumRow))):
            if count == 1:
                self.__assignInRow(location, x)

    def __assignCol(self, location):
        """
            (Private method) Assign all possibilities to the location in all columns
        """
        sumCol = []
        for x in self.__colLocations(self.__col(location)):
            if len(self.sudoku[x]) != 1:
                sumCol.extend(self.sudoku[x])
        sumCol.sort()
        for x, count in list(set(map(lambda x:(x, sumCol.count(x)), sumCol))):
            if count == 1:
                self.__assignInCol(location, x)

    def __assignSub(self, location):
        """
            (Private method) Assign all possibilities to the location in all subgrids
        """
        sumSub = []
        for x in self.__subLocations(self.__sub(location)):
            if len(self.sudoku[x]) != 1:
                sumSub.extend(self.sudoku[x])
        sumSub.sort()
        for x, count in list(set(map(lambda x:(x, sumSub.count(x)), sumSub))):
            if count == 1:
                self.__assignInSub(location, x)

    def __assign(self, location):
        """
            (Private method) Assign all possibilities to the location
        """
        self.__assignRow(location)
        self.__assignCol(location)
        self.__assignSub(location)

    def solveOneStep(self):
        """
            Set one step towards solving the Sudoku
        """
        for x in range(self.size ** 2):
            if len(self.sudoku[x]) == 1:
                self.__removePossiblity(x, self.sudoku[x][0])
            else:
                self.__assign(x)

    def solve(self, maxSteps = 20):
        """
            Solve the Sudoku by setting steps towards solving, until the maxSteps is reached. Default maxSteps = 20
        """
        steps = 0
        while not self.isSolved():
            self.solveOneStep()
            if self.mode == DEBUG_MODE:
                self.print()
            steps += 1

            if steps > maxSteps:
                print(f"Could not solve in {maxSteps} steps")
                break
        
        return self.sudoku
