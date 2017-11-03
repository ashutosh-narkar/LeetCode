#!/usr/bin/env python
'''
Given a 2D board containing 'X' and 'O', capture all regions surrounded by 'X'.

A region is captured by flipping all 'O's into 'X's in that surrounded region.

For example,
X X X X
X O O X
X X O X
X O X X
After running your function, the board should be:

X X X X
X X X X
X X X X
X O X X


Solution:
Because the boundary 'O' are definitely "live" (have a path out) element, so, we BFS from each 'O' in the boundary, 
mark all its four directions (where is also 'O') as "live". 

Last step is to flip "O" to "X" because there is no way out

'''
from collections import deque



# @param board, a 2D array
# Capture all regions by modifying the input board in-place.

def solve(board):

    if not board:
        return


    nrows = len(board)
    ncols = len(board[0])

    bb = [[False] * ncols for i in range(nrows)]
    queue = deque()


    for i in range(ncols):
        if board[0][i] == 'O':
            bb[0][i] = True
            queue.append((0, i))


        if board[nrows - 1][i] == 'O':
            bb[nrows - 1][i] = True
            queue.append((nrows - 1, i))


    for i in range(nrows):
        if board[i][0] == 'O':
            bb[i][0] = True
            queue.append((i,0))

        if board[i][ncols -1] == 'O':
            bb[i][ncols - 1] = True
            queue.append((i, ncols - 1))

            
    while queue:
        row, col = queue.popleft()

        # up
        if isFree(board, row - 1, col) and not bb[row - 1][col]:
            bb[row - 1][col] = True
            queue.append((row - 1, col))


        # down
        if isFree(board, row + 1, col) and not bb[row + 1][col]:
            bb[row + 1][col] = True
            queue.append((row + 1, col))

            
        # left
        if isFree(board, row, col - 1) and not bb[row][col - 1]:
            bb[row][col - 1] = True
            queue.append((row, col - 1))


        # right
        if isFree(board, row, col + 1) and not bb[row][col + 1]:
            bb[row][col + 1] = True
            queue.append((row, col + 1))


    for i  in range(nrows):
        for j in range(ncols):
            if board[i][j] == 'O' and not bb[i][j]:
                board[i][j] = 'X'


def isFree(board, row, col):

    if 0 <= row < len(board) and 0 <= col < len(board[0]) and board[row][col] == 'O':
        return True

    return False


    

    

    
