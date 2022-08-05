# Sudoku Solver
This soduku solver is used to solve a standard Sudoku containing 81 cells, in a 9×9 grid, and has 9 boxes, each box being the intersection of the first, middle, or last 3 rows, and the first, middle, or last 3 columns. Each cell may contain a number from one to nine, and each number can only occur once in each row, column, and box.

Basically in sudoku, we want to be able to solve a sudoku puzzle given an input like this, 
which represents a sudoku board:
```
[[x00, x01, x02, x03... x08],
 [x10, x11, x12, x13... x18],
 ...
 [x80, x81, x82, x83... x88]]
```
These x_rc values correspond to the value at the rth row, cth column (starting with 0-index)
These values could be empty (we will represent this with -1)

So for example,
```
[[-1,  1,  5, ...],
 [-1, -1, -1, ...],
 [ 6, -1, -1, ...]
 ...]
```
would represent a board like this:
```
 -----------
|     1   5 | ...
|           | ...
| 6         | ...
 -----------
 ...
```