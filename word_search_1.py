#!/usr/bin/env python
'''
Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are
those horizontally or vertically neighboring.

The same letter cell may not be used more than once.

For example,
Given board =

[
  ["ABCE"],
  ["SFCS"],
  ["ADEE"]
]
word = "ABCCED", -> returns true,
word = "SEE", -> returns true,
word = "ABCB", -> returns false.
'''

# Runtime: O(4^n) since we are recursively traversing the 4 adjacent cells at each step

def exist(board, word):
    """
    :type board: List[List[str]]
    :type word: str
    :rtype: bool
    """
    if not board:
        return False

    for i in range(len(board)):
        for j in range(len(board[0])):
            if dfs(board, word, i, j):
                return True

    return False


# check whether we can find word, start at (row,col) position
def dfs(board, word, row, col):
    if not word:  # all the characters are checked
        return True

    # invalid rows
    if row < 0 or row >= len(board):
        return False

    # invalid columns
    if col < 0 or col >= len(board[0]):
        return False

    # character mismatch
    if word[0] != board[row][col]:
        return False

    tmp = board[row][col]  # first character is found, check the remaining part
    board[row][col] = "."  # avoid visit again

    # check whether we can find "word" along one direction
    res = dfs(board, word[1:], row - 1, col) or \
          dfs(board, word[1:], row + 1, col) or \
          dfs(board, word[1:], row, col - 1) or \
          dfs(board, word[1:], row, col + 1)

    board[row][col] = tmp
    return res
