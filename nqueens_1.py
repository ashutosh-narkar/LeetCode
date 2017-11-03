#!/usr/bin/env python
'''
The n-queens puzzle is the problem of placing n queens on an n×n chessboard such that no two queens attack each other.
Given an integer n, return all distinct solutions to the n-queens puzzle.

Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space respectively.

For example,
There exist two distinct solutions to the 4-queens puzzle:

[
 [".Q..",  // Solution 1
  "...Q",
  "Q...",
  "..Q."],

 ["..Q.",  // Solution 2
  "Q...",
  "...Q",
  ".Q.."]
]

Solution:
1. Use a int vector to store the current state,  A[i]=j refers that the ith row and jth column is placed a queen.
2. Valid state:  not in the same column, which is A[i]!=A[current], not in the same diagonal direction: abs(A[i]-A[current]) != r-i

3. Recursion: 
       Start:   placeQueen(0,n)
        if current ==n then print result
        else
            for each place less than n,
                 place queen
                if current state is valid, then place next queen   place Queen(cur+1,n)
           end for
        end if



Alternate Questions:
1) Compute a placement of 32 knights, or 14 bishops, 16 kings or eight
rooks on an 8 × 8 chessboard in which no two pieces attack each other.

2) Compute the smallest number of queens that can be placed to attack
each uncovered square

'''


def solveNQueens(n):

    if not n:
        return []


    result = []

    # entire row
    pos  = [-1] * n


    dfs(pos, 0, n, result)
    return result


def dfs(pos, row, n, result):


    if row == n:
        res = []
        for i in range(n):
            temp = ['.'] * n
            # place queen at proper col
            temp[pos[i]] = 'Q' 
            temp = ''.join(temp)
            res.append(temp)

        result.append(res)

        

    else:
        for i  in range(n):
            pos[row] = i

            if isValid(pos, row):
                dfs(pos, row + 1, n, result)
                

def isValid(pos, r):
    for i in range(r):
        if (pos[i] == pos[r]) or abs(pos[i] - pos[r]) == r - i:
            return False

    return True
