{-- 
    SudokuSolver
    main.hs

    Thijs Dregmans
    Version: 4.0
    Last edited: 2024-02-21

    Goal is to create a Haskell program that automatically solves sudokus. 
    It does this with an algorithm that I belief to be logical and efficient. 
    The used algorithm may change later, because other puzzles - with a 
    greater difficulty - require it. 

--}

module Main where
    
    import Data.List

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



    type Sudoku = [[Integer]]
    type SudokuRow = [[Integer]]
    type SudokuColumn = [[Integer]]

    example :: Sudoku
    example = 
        [
            [1],[ ],[ ], [ ],[ ],[ ], [8],[ ],[ ],
            [4],[5],[ ], [7],[ ],[1], [ ],[ ],[9],
            [6],[ ],[8], [3],[ ],[2], [7],[ ],[5],

            [ ],[ ],[ ], [ ],[5],[3], [ ],[9],[ ],
            [5],[2],[ ], [ ],[ ],[8], [1],[ ],[3],
            [8],[ ],[9], [ ],[1],[ ], [ ],[4],[2],
            
            [ ],[8],[7], [4],[6],[ ], [ ],[ ],[ ],
            [ ],[ ],[5], [ ],[7],[2], [3],[8],[ ],
            [2],[ ],[ ], [ ],[ ],[ ], [4],[5],[ ]
        ]

    -- solved returns True if the sudoku is solved and False if it is not.
    isSolved :: Sudoku -> Bool
    isSolved sudoku = maximum lengths == 1 && minimum lengths == 1
        where lengths = map length sudoku


    -- Sudoku's must be initializes before they can be solved
    initSudoku :: Sudoku -> Sudoku
    initSudoku sudoku = map (\f -> if null f then [1..9] else f) sudoku

    -- Retrieve a single row by pointer from a Sudoku. The pointer is zero-indexed.
    row :: Sudoku -> Int -> SudokuRow
    row sudoku pointer = take (9) . drop (9*(pointer)) $ sudoku

    -- Retrieve a single column by pointer from a Sudoku. The pointer is zero-indexed.
    column :: Sudoku -> Int -> SudokuRow
    column sudoku pointer = take (9) . drop (9*(pointer)) $ sudoku

    {-- 
        Sudoku's get solved piece by piece. This algorithm assigns all possible values to a field, while eliminating values that are no longer possible. If this process is repeated long enough, all fields will have only one possible value - which is the actual value. 
        The `eliminate` function removes the possible values that are no longer possible in each field.
    --}
    -- eliminate :: Sudoku -> Sudoku
    -- eliminate sudoku = map (\f -> if null f then deleteBy (sudoku) f else f) sudoku

    -- eliminateField :: [Integer] -> Sudoku -> [Integer]
    -- eliminateField possibilities sudoku = 

    -- assign :: Sudoku -> Sudoku
    -- assign sudoku = 

    -- Note: for the following help functions, the sudoku cannot have no possibilities. checkPossibilities has to fill them in. Maybe by invoking another function. 
    -- checkRow :: sudoku -> sudoku 
    -- checkRow sudoku = map (/r -> (/f -> if length f == 1 then {—- delete [(f !! 0)] r )) sudoku

    -- checkCol :: sudoku -> sudoku 
    -- checkCol sudoku =

    -- checkBox :: sudoku -> sudoku 
    -- checkBox sudoku =

    main = do
        -- initialise Sudoku
        -- let example = 
        --         [
        --             [1],[ ],[ ], [ ],[ ],[ ], [8],[ ],[ ],
        --             [4],[5],[ ], [7],[ ],[1], [ ],[ ],[9],
        --             [6],[ ],[8], [3],[ ],[2], [7],[ ],[5],

        --             [ ],[ ],[ ], [ ],[5],[3], [ ],[9],[ ],
        --             [5],[2],[ ], [ ],[ ],[8], [1],[ ],[3],
        --             [8],[ ],[9], [ ],[1],[ ], [ ],[4],[2],
                    
        --             [ ],[8],[7], [4],[6],[ ], [ ],[ ],[ ],
        --             [ ],[ ],[5], [ ],[7],[2], [3],[8],[ ],
        --             [2],[ ],[ ], [ ],[ ],[ ], [4],[5],[ ]
        --         ]

        let s = initSudoku example 
        
        if (isSolved example) then 
            putStrLn "is solved"
        else
            putStrLn "not solved"
        putStrLn "done"
