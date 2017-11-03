#!/usr/bin/env python
'''
Design a Tic-tac-toe game that is played between two players on a n x n grid.

Solution:
Record the number of moves for each rows, columns, and two diagonals.
For each move, we -1 for each player 1's move and +1 for player 2's move.
Then we just need to check whether any of the recorded numbers equal to n or -n.
'''


class TicTacToe(object):
    def __init__(self, n):
        self.row, self.col, self.diag, self.anti_diag, self.n = [0] * n, [0] * n, 0, 0, n

    def move(self, row, col, player):
        score = player * 2 - 3

        self.row[row] += score
        self.col[col] += score

        # diagonal
        if row == col:
            self.diag += score

        # anti-diagonal
        if row + col == self.n - 1:
            self.anti_diag += score

        # player 2 wins
        if self.n in [self.row[row], self.col[col], self.diag, self.anti_diag]:
            return 2

        # player 1 wins
        if -self.n in [self.row[row], self.col[col], self.diag, self.anti_diag]:
            return 1

        return 0
