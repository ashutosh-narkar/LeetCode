#!/usr/bin/env python
'''
Determine if a Sudoku is valid, according to: Sudoku Puzzles - The Rules.

The Sudoku board could be partially filled, where empty cells are filled with the character '.'.

A valid Sudoku board (partially filled) is not necessarily solvable. Only the filled cells need to be validated.
'''
def isValidSudoku(board):

    if not board:
        return False

    return (is_row_valid(board) and
            is_col_valid(board) and
            is_square_valid(board))



def is_row_valid(board):
    for row in board:
        if not is_unit_valid(row):
            return False
    return True


def is_col_valid(board):
    for col in zip(*board):               #### nice way to get columns
        if not is_unit_valid(col):
            return False
    return True



# check each 3*3 matrix
def is_square_valid(board):
    for i in (0, 3, 6):
        for j in (0, 3, 6):
            square = [board[x][y] for x in range(i, i + 3) for y in range(j, j + 3)]
            if not is_unit_valid(square):
                return False
    return True


def is_unit_valid(unit):
    unit = [i for i in unit if i != '.']
    return len(set(unit)) == len(unit)
