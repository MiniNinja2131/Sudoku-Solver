def findNextEmpty(puzzle):
    # Finds the next row, col on the puzzle that's not filled yet -> in our scenario, -1 is used to represent an empty space
    # Return row, col tuple or (None, None) if there is none ~> no spaces on the sudoku board

    # Keep in mind that we are using 0-8 indices
    for r in range(9):
        for c in range(9):
            if puzzle[r][c] == -1:
                return r, c
    # If there are no spaces in the puzzle are empty (indicated by the -1)
    return None, None

def isValid(puzzle, guess, row, col):
    # Figures out whether the guess at the row/col of the puzzle is a valid guess
    # Return true if its valid, false otherwise

    # See if theres an duplicate number in that row:
    rowVals = puzzle[row]
    if guess in rowVals:
        return False
    
    # Checking validation with column
    #colVals = []
    #for i in range(9):
    #    colVals.append(puzzle[i][col])
    # The statement below is essentially replicating the statement above!
    colVals = [puzzle[i][col] for i in range(9)]
    if guess in colVals:
        return False

    # Validation for each individual squares
    # We want to know where the 3x3 square starts and interate over the 3 values in the row/column
    # For example 1 // 3 = 0, where 5 // 3 = 1 since 3 goes into 5 once
    rowStart = (row // 3) * 3
    colStart = (col // 3) * 3

    for r in range(rowStart, rowStart + 3):
        for c in range(colStart, colStart + 3):
            if puzzle[r][c] == guess:
                return False
                
    return True

def solveSudoku(puzzle):
    # Solve sudoku using backtracking
    # Puzzle is a list of lists where each inner list is a row in our sudoku puzzle
    # Return whether a solution exits or not

    # Step 1: Choose somewhere on the puzzle to make a guess
    row, col = findNextEmpty(puzzle)

    # Step 1.1: If there's nowhere left, then we're done because only allowed valid inputs
    if row is None:
        return True
    
    # Step 2: If there is a place to put a number, then make a guess between 1-9
    # Where range(1,10) -> 1,2,3,4...,9
    for guess in range(1,10):
        # Step 3: Check if this is valid guess
        if isValid(puzzle, guess, row, col):
            # Step 3.1: If this is valid, then place that guess on the puzzle
            puzzle[row][col] = guess
            # Now recursively using this puzzle
            # Step 4: recursively call our function
            if solveSudoku(puzzle):
                return True
        # Step 5: if not valid OR if our guess does not solve the puzzle, then we need to backtract and try a new number
        # To reset we are replacing it with -1 i.e an empty space again
        puzzle[row][col] = -1
        
    # Step 6: If none of the numbers that we try work, then this puzzle is unsolvable
    return False

if __name__ == '__main__':
    # Example of completable board that the solver could solve
    exampleBoard = [
        [3, 9, -1,   -1, 5, -1,   -1, -1, -1],
        [-1, -1, -1,   2, -1, -1,   -1, -1, 5],
        [-1, -1, -1,   7, 1, 9,   -1, 8, -1],

        [-1, 5, -1,   -1, 6, 8,   -1, -1, -1],
        [2, -1, 6,   -1, -1, 3,   -1, -1, -1],
        [-1, -1, -1,   -1, -1, -1,   -1, -1, 4],

        [5, -1, -1,   -1, -1, -1,   -1, -1, -1],
        [6, 7, -1,   1, -1, 5,   -1, 4, -1],
        [1, -1, 9,   -1, -1, -1,   2, -1, -1]
    ]
    print(solveSudoku(exampleBoard))
    print(exampleBoard)