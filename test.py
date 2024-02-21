example = [[1],[],[], [],[],[], [8],[],[],
           [4],[5],[], [7],[],[1], [],[],[9],
           [6],[],[8], [3],[],[2], [7],[],[5],

           [],[],[], [],[5],[3], [],[9],[],
           [5],[2],[], [],[],[8], [1],[],[3],
           [8],[],[9], [],[1],[], [],[4],[2],
           
           [],[8],[7], [4],[6],[], [],[],[],
           [],[],[5], [],[7],[2], [3],[8],[],
           [2],[],[], [],[],[], [4],[5],[]]


def init(sudoku):
    for index in range(0, len(sudoku)):
        if len(sudoku[index]) == 0:
            sudoku[index] = [x for x in range(9)]

def eliminateInRow(sudoku, value, baseIndex):
    for index in range(0, len(sudoku)):
        if index // 9 == baseIndex // 9:
            # field is in the same row
            print(index)
            print(baseIndex)
            print(sudoku[index])
            print(value)
            sudoku[index].remove(value)

def eliminate(sudoku):
    for index in range(0, len(sudoku)):
        if len(sudoku[index]) == 0:
            init(example)
        if len(sudoku[index]) == 1:
            eliminateInRow(sudoku, sudoku[index][0], index)
            print("000")

init(example)
print(example[0:8])

# eliminate(example)
eliminateInRow(example, example[0][0], 0)