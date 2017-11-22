#!/usr/bin/env python
"""
According to the Wikipedia's article: "The Game of Life, also known simply as Life, is a cellular automaton devised
by the British mathematician John Horton Conway in 1970."

Given a board with m by n cells, each cell has an initial state live (1) or dead (0).
Each cell interacts with its eight neighbors (horizontal, vertical, diagonal) using the following four rules:

1. Any live cell with fewer than two live neighbors dies, as if caused by under-population.
2. Any live cell with two or three live neighbors lives on to the next generation.
3. Any live cell with more than three live neighbors dies, as if by over-population..
4. Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.

Write a function to compute the next state (after one update) of the board given its current state.

Solution:
To solve it in place, we use 2 bits to store 2 states:

[2nd bit, 1st bit] = [next state, current state]

- 00  dead (next) <- dead (current)
- 01  dead (next) <- live (current)
- 10  live (next) <- dead (current)
- 11  live (next) <- live (current)


For each cell's 1st bit, check the 8 pixels around itself, and set the cell's 2nd bit.

Transition 01 -> 11: when board == 1 and lives >= 2 && lives <= 3.
Transition 00 -> 10: when board == 0 and lives == 3.

To get the current state: board[i][j] & 1

To get the next state: board[i][j] >> 1

Since in the beginning, every 2nd bit is 0, we only care about Rule 2 and Rule 4.
"""


def gameOfLife(board):
    """
    :type board: List[List[int]]
    :rtype: void Do not return anything, modify board in-place instead.
    """
    if not board:
        return

    nrows = len(board)
    ncols = len(board[0])

    for i in range(nrows):
        for j in range(ncols):
            lives = liveNeighbors(board, i, j)

            # In the beginning, every 2nd bit is 0;
            # So we only need to care about when will the 2nd bit become 1
            if board[i][j] == 1 and 2 <= lives <= 3:
                board[i][j] = 3

            if board[i][j] == 0 and lives == 3:
                board[i][j] = 2

    for i in range(nrows):
        for j in range(ncols):
            board[i][j] >>= 1  # Get the 2nd state


def liveNeighbors(board, row, col):
    lives = 0

    # VERY COOL WAY TO GET THE NEIGHBOURING VALUES
    row_boundary_up = max(row - 1, 0)
    row_boundary_down = min(row + 1, len(board) - 1)

    col_boundary_left = max(col - 1, 0)
    col_boundary_right = min(col + 1, len(board[0]) - 1)

    for x in range(row_boundary_up, row_boundary_down + 1):         # plus '1' since we include row_boundary_down index
        for y in range(col_boundary_left, col_boundary_right + 1):  # plus '1' since we include col_boundary_right index
            lives += board[x][y] & 1

    lives -= board[row][col] & 1      # remove self value
    return lives
