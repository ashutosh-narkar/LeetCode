#!/usr/bin/env python
'''
Follow up for N-Queens problem.

Now, instead outputting board configurations, return the total number of distinct solutions.
'''
def totalNQueens(n):

    if not n:
        return 0


    result = [0]        # need to pass 'list' in recursion

    # entire row
    pos  = [-1] * n

    dfs(pos, 0, n, result)
    return result[0]


def dfs(pos, row, n, result):

    if row == n:
        result[0] += 1


    else:
        for i  in range(n):
            pos[row] = i

            # place next queen
            if isValid(pos, row):
                dfs(pos, row + 1, n, result)


def isValid(pos, r):
    for i in range(r):
        if (pos[i] == pos[r]) or abs(pos[i] - pos[r]) == r - i:
            return False

    return True
