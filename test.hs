{-- 
    Sudoku solver

    Thijs Dregmans
    Version: 2.0
    Last edited: 2023-07-21

    Goal is to create a Haskell program that automatically solves sudokus. 
    It does this with an algorithm that I belief to be logical and efficient. 
    The used algorithm may change later, because other puzzles - with a 
    greater difficulty - require it. 

--}

{-- 
    The format of the sudoku are represented by the type sudoku; or 
    in other words [[Integer]]. The first - outer - list contains the 
    fields of the sudoku. The rows and columns are represented by one list; 
    the items going from the top-left to the right-bottom. The fields are also 
    lists. They contain all the possibilities for that field. If a field has a 
    definite value, it therefore only contains one Integer. At the start of 
    runtime, all the empty fields are assigned [1..sizeX*sizeY] by 
    checkPossibilities. Almost always, this turns out to be [1..9]. 
    See the explanation of checkPossibilities for more information.
--}

import Data.List

type Sudoku = [[Integer]]

example :: Sudoku
example = [[1],[],[], [],[],[], [8],[],[],
           [4],[5],[], [7],[],[1], [],[],[9],
           [6],[],[8], [3],[],[2], [7],[],[5],

           [],[],[], [],[5],[3], [],[9],[],
           [5],[2],[], [],[],[8], [1],[],[3],
           [8],[],[9], [],[1],[], [],[4],[2],
           
           [],[8],[7], [4],[6],[], [],[],[],
           [],[],[5], [],[7],[2], [3],[8],[],
           [2],[],[], [],[],[], [4],[5],[]]

-- solved returns True if the sudoku is solved and False if it is not.

-- solved :: sudoku -> Bool
-- solved sudoku = maximum lengths == 1 && minimum length == 1
--     where lengths = map length sudoku


-- solveOneSteps solves the entered sudoku with one step. 
-- By repeatingly calling this function, the whole sudoku gets solved. It puts out the sudoku. 

solveOneStep :: Sudoku -> Sudoku
solveOneStep sudoku = [[2]]

initSudoku :: Sudoku -> Sudoku
initSudoku sudoku = map (\f -> if null f then [1..9] else f) sudoku

ex2 :: Sudoku
ex2 = initSudoku example


eliminate :: Sudoku -> Sudoku
eliminate sudoku = map (\f -> if null f then deleteBy (sudoku) f else f) sudoku

-- eliminateField :: [Integer] -> Sudoku -> [Integer]
-- eliminateField possibilities sudoku = 

-- assign :: Sudoku -> Sudoku
-- assign sudoku = 

-- -- Note: for the following help functions, the sudoku cannot have no possibilities. checkPossibilities has to fill them in. Maybe by invoking another function. 
-- checkRow :: sudoku -> sudoku 
-- checkRow sudoku = map (/r -> (/f -> if length f == 1 then {—- delete [(f !! 0)] r )) sudoku

-- checkCol :: sudoku -> sudoku 
-- checkCol sudoku =

-- checkBox :: sudoku -> sudoku 
-- checkBox sudoku =
