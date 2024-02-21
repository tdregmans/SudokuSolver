# SudokuSolver

I came up with this idea, during the holidays. I solved a couple of sudoku's and asked myself if I could write a program that could do the same.
I think I can. My implementation of my own algoritm is done in Python. 

## The algoritm
A normal sudoku is a puzzle with 3 by 3 grids of 3 by 3. Each row and column is unique. They are filled by numbers from 1 to 9. Each number has to be used 9 times. Each column has to contain all the numbers once. Each row has to contain all the numbers once. Each subgrid has to contain all the numbers once.

At the start, there are some numbers already filled in. They restrict the possibilities to such an extend, that only one solution works.

My algoritm is based on this thought: "At the start, a field has 9 possibilities. During the solving process, the possibilities are eliminated." At the start, all empty fields are assigned lists of `[1..9]`. Then, the possibilities are restricted by the already known values. The known values are represented by lists with only one value.

The algoritm has 2 main phases:

### 1. The elimination phase

During the elimination phase, we eliminate all the values that are no longer possible. We go through all the rows and eliminate all the possibilities that correspond with the known values in that row. We do the same for the columns and subgrids.

### 2. The assignment phase

During the assignment phase, we account for the second criteria that can make a value definitive. A field's value is definitive if;
- the field only has one possibility, or if;
- the value only has one possible location.
The first phase eliminates all the values that are no longer possible in that row, column and subgrid, for each field. At some point, only one possible value will remain. This becomes the definitive value, automatically. It is also possible that a value only is possible in one field in a row, column or subgrid. This value is assigned to this field, by removing all other possibilities.

### 3. The advanced-elimination phase
There are also some other methods we can use to eliminate possibilities. Those are used in this phase.

An example of this:

If in a row, column or subgrid, the position of x and y are unsure, and there are only two possibilities for x and two possibilities for y in that row, column or subgrid, then all the other possibilities of x and y can be eliminated in the other space.
If we have an almost completed row, but `2` and `7` are missing, and those values are in the same subgrid, we know that we need to put an `2` and `7` in the row so all other possibilities for `2` and `7` can be eliminated in that subgrid.

---

Right now, I use the phases 1 and 2 succeeding. In the future, I can add phase 3 and call the steps only when needed to increase efficiency.

## Status

This project is still under development. The [latest version](https://github.com/tdregmans/SudokuSolver/releases/latest) can be found on Github.