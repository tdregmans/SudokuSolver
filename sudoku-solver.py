# test sudoku solver

# version 3
# Thijs Dregmans
# 2023-07-27

size = 9

# sudoku = [[1],[ ],[ ], [ ],[ ],[ ], [8],[ ],[ ],
#           [4],[5],[ ], [7],[ ],[1], [ ],[ ],[9],
#           [6],[ ],[8], [3],[ ],[2], [7],[ ],[5],

#           [ ],[ ],[ ], [ ],[5],[3], [ ],[9],[ ],
#           [5],[2],[ ], [ ],[ ],[8], [1],[ ],[3],
#           [8],[ ],[9], [ ],[1],[ ], [ ],[4],[2],

#           [ ],[8],[7], [4],[6],[ ], [ ],[ ],[ ],
#           [ ],[ ],[5], [ ],[7],[2], [3],[8],[ ],
#           [2],[ ],[ ], [ ],[ ],[ ], [4],[5],[ ]]

# sudoku = [[ ],[ ],[ ], [ ],[ ],[ ], [ ],[ ],[ ],
#           [ ],[ ],[ ], [ ],[ ],[ ], [ ],[ ],[ ],
#           [ ],[ ],[ ], [ ],[ ],[ ], [ ],[ ],[ ],

#           [ ],[ ],[ ], [ ],[ ],[ ], [ ],[ ],[ ],
#           [ ],[ ],[ ], [ ],[ ],[ ], [ ],[ ],[ ],
#           [ ],[ ],[ ], [ ],[ ],[ ], [ ],[ ],[ ],

#           [ ],[ ],[ ], [ ],[ ],[ ], [ ],[ ],[ ],
#           [ ],[ ],[ ], [ ],[ ],[ ], [ ],[ ],[ ],
#           [ ],[ ],[ ], [ ],[ ],[ ], [ ],[ ],[ ]]

# sudoku = [[ ],[4],[ ], [ ],[ ],[ ], [ ],[5],[ ],
#           [1],[ ],[ ], [5],[ ],[ ], [7],[ ],[ ],
#           [9],[ ],[ ], [ ],[7],[ ], [ ],[4],[6],

#           [ ],[ ],[5], [ ],[8],[1], [ ],[ ],[ ],
#           [ ],[ ],[ ], [6],[ ],[ ], [ ],[ ],[4],
#           [ ],[ ],[ ], [9],[5],[ ], [ ],[2],[ ],

#           [ ],[ ],[ ], [ ],[ ],[ ], [ ],[ ],[ ],
#           [ ],[ ],[ ], [1],[9],[8], [ ],[ ],[2],
#           [6],[ ],[2], [7],[4],[ ], [8],[9],[ ]]

sudoku = [[5],[ ],[ ], [1],[ ],[ ], [ ],[ ],[ ],
          [7],[1],[ ], [3],[ ],[ ], [ ],[ ],[8],
          [ ],[3],[ ], [ ],[5],[ ], [ ],[7],[ ],

          [ ],[8],[ ], [7],[ ],[1], [ ],[ ],[5],
          [ ],[2],[ ], [4],[ ],[ ], [ ],[3],[ ],
          [ ],[ ],[ ], [ ],[ ],[ ], [ ],[ ],[4],

          [ ],[ ],[6], [ ],[ ],[4], [ ],[8],[1],
          [ ],[ ],[2], [ ],[ ],[ ], [ ],[ ],[ ],
          [1],[ ],[ ], [ ],[ ],[ ], [6],[9],[3]]

def enterSudoku():
    print("Enter in a sudoku.")
    print("Enter the fields row by row, from left to right.")
    print("If a field is empty, enter nothing i.e. ''")
    
    sudoku = []
    printSudoku()
    for field in range(size * size):
        i = input("Enter field " + str(field) + ": ")
        if i == "":
            sudoku.append([])
        else:
            sudoku.append([int(i)])
    printSudoku()
    i = input("Is the correct? (y/n) ")
    if i == 'y':
        return
    else:
        print("retry")
        enterSudoku()


def printSudoku():
    print("sudoku")
    print(size * "-_-_")
    for x in range(size ** 2):
        if len(sudoku[x]) == 1:
            print(str(sudoku[x][0]) + "   ", end='')
        else:
            print("x   ", end='')
        if x % 9 == 8:
            print()

def printRowColSub(f):
    # f can be the `row`, `col` or `sub` function
    print(size * "-_-_")
    for x in range(size ** 2):
        print(str(f(x)) + "   ", end='')
        if x % 9 == 8:
            print()

def solved():
    for x in range(size ** 2):
        if len(sudoku[x]) != 1:
            return False
    return True

def fillWholeSudokuWithAllPossibilities():
    for x in range(size ** 2):
        sudoku.append(list(range(1, size + 1)))

def init():
    for x in range(size ** 2):
        if len(sudoku[x]) == 0:
            sudoku[x] = (list(range(1, size + 1)))

def row(location):
    # return the id of the row that location is located in
    return location // size

def col(location):
    # return the id of the col that location is located in
    return location % size

def sub(location):
    # return the id of the subGrid that location is located in
    return (row(location) // 3) * 3 + (col(location) // 3)

def rowLocations(id):
    # return a list with all locations of the row with the specified id
    return list(range(id * size, id * size + size))

def colLocations(id):
    # return a list with all location of the columns with the specified id
    return list(range(id, size*size, size))

def subLocations(id):
    firstFieldInSub = ((id // 3) * 3) * 9 + ((id % 3) * 3)
    return [firstFieldInSub, firstFieldInSub + 1, firstFieldInSub + 2,
            firstFieldInSub + 9, firstFieldInSub + 10, firstFieldInSub + 11,
            firstFieldInSub + 18, firstFieldInSub + 19, firstFieldInSub + 20]

def removePossiblityRow(location, possibility):
    for x in rowLocations(row(location)):
        if possibility in sudoku[x] and len(sudoku[x]) != 1:
            sudoku[x].remove(possibility)

def removePossiblityCol(location, possibility):
    for x in colLocations(col(location)):
        if possibility in sudoku[x] and len(sudoku[x]) != 1:
            sudoku[x].remove(possibility)

def removePossiblitySub(location, possibility):
    for x in subLocations(sub(location)):
        if possibility in sudoku[x] and len(sudoku[x]) != 1:
            sudoku[x].remove(possibility)
            

def removePossiblity(location, possibility):
    removePossiblityRow(location, possibility)
    removePossiblityCol(location, possibility)
    removePossiblitySub(location, possibility)

def assignInRow(location, possibility):
    for x in rowLocations(row(location)):
        if possibility in sudoku[location] and len(sudoku[x]) != 1:
            sudoku[x] = [possibility]
            return
        
def assignInCol(location, possibility):
    for x in colLocations(col(location)):
        if possibility in sudoku[location] and len(sudoku[x]) != 1:
            sudoku[x] = [possibility]
            return
        
def assignInSub(location, possibility):
    for x in subLocations(sub(location)):
        if possibility in sudoku[location] and len(sudoku[x]) != 1:
            sudoku[x] = [possibility]
            return

def assignRow(location):
    sumRow = []
    for x in rowLocations(row(location)):
        if len(sudoku[x]) != 1:
            sumRow.extend(sudoku[x])
    sumRow.sort()
    for x, count in list(set(map(lambda x:(x, sumRow.count(x)), sumRow))):
        if count == 1:
            assignInRow(location, x)

    

def assignCol(location):
    sumCol = []
    for x in colLocations(col(location)):
        if len(sudoku[x]) != 1:
            sumCol.extend(sudoku[x])
    sumCol.sort()
    for x, count in list(set(map(lambda x:(x, sumCol.count(x)), sumCol))):
        if count == 1:
            assignInCol(location, x)

def assignSub(location):
    sumSub = []
    for x in subLocations(sub(location)):
        if len(sudoku[x]) != 1:
            sumSub.extend(sudoku[x])
    sumSub.sort()
    for x, count in list(set(map(lambda x:(x, sumSub.count(x)), sumSub))):
        if count == 1:
            assignInSub(location, x)

def assign(location):
    assignRow(location)
    assignCol(location)
    assignSub(location)


def go():
    for x in range(size ** 2):
        if len(sudoku[x]) == 1:
            removePossiblity(x, sudoku[x][0])
        else:
            assign(x)

# enterSudoku()

init()
printSudoku()

go()
printSudoku()


steps = 0
while not solved():
    go()
    printSudoku()
    steps += 1

    if steps > 10:
        print("Could not solve in 10 steps")
        break
