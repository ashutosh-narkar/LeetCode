#!/usr/bin/env python
'''
Write a program to solve a Sudoku puzzle by filling the empty cells.
Empty cells are indicated by the character '.'.

You may assume that there will be only one unique solution.
'''

# @param board, a 9x9 2D array
# Solve the Sudoku by modifying the input board in-place.
# Do not return any value.

def solveSudoku(board):
	if not board:
		return

	solved(board)


def solved(board):
    
    for row in range(len(board)):
	for col in range(len(board[0])):
	    if board[row][col] == '.':
		for num in range(1, 10):
		    if self.isValid(board, row, col, str(num)):
			board[row][col] = str(num)

			if self.solved(board):
			    return True
			else:
			    board[row][col] = '.'    


		# if no proper number found, return false        
		return False

    return True


def isValid(self, board, row, col, char):

    # check row
    for i in range(len(board)):
	if board[i][col] == char:
	    return False

	    
    # check col
    for i in range(len(board[0])):
	if board[row][i] == char:
	    return False

	    

    # check block
    boxrow = row - row%3
    boxcol = col - col%3

    for i in range(boxrow, boxrow + 3):
	for j in range(boxcol, boxcol + 3):
	    if board[i][j] == char:
		return False
    

    return True
