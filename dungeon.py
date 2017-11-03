#!/usr/bin/env python
'''
The demons had captured the princess (P) and imprisoned her in the bottom-right corner of a dungeon. 
The dungeon consists of M x N rooms laid out in a 2D grid. 
Our valiant knight (K) was initially positioned in the top-left room and must fight his
way through the dungeon to rescue the princess.

The knight has an initial health point represented by a positive integer.
If at any point his health point drops to 0 or below, he dies immediately.

Some of the rooms are guarded by demons, so the knight loses health (negative integers) upon entering these rooms; 
other rooms are either empty (0's) or contain magic orbs that increase the knight's health (positive integers).

In order to reach the princess as quickly as possible, the knight decides to move only rightward or downward in each step.


Write a function to determine the knight's minimum initial health so that he is able to rescue the princess.

For example, given the dungeon below, the initial health of the knight must be at least 7 if he follows the optimal path RIGHT-> RIGHT -> DOWN -> DOWN.

-2(K)  -3    3
-5     -10   1
10     30   -5(P)

Notes:

The knight's health has no upper bound.
Any room can contain threats or power-ups, even the first room the knight enters and
the bottom-right room where the princess is imprisoned.
'''

def calculateMinimumHP(dungeon):

    if not dungeon:
        return 0

    nrows = len(dungeon)
    ncols = len(dungeon[0])

    dp = [0] * ncols

    for i in range(nrows - 1, -1, -1):
        for j in range(ncols - 1, -1, -1):

            # for the last battle in the last room, we need atleast 1 more point than the point in that cell
            if i == nrows - 1 and j == ncols - 1:
                dp[j] = 1 - dungeon[i][j]

            # in the last row, knight can only move right, so we can compute health value using right neighbour
            elif i == nrows - 1:
                dp[j] = dp[j + 1] - dungeon[i][j]

            # in the last col, knight can only move down, so we can compute health value using downward neighbour
            elif j == ncols - 1:
                dp[j] = dp[j] - dungeon[i][j]

            # others
            else:
                dp[j] = min(dp[j + 1], dp[j]) - dungeon[i][j]

            # we need atleast power of 1
            if dp[j] <= 0:
                dp[j] = 1

                

    return dp[0]

    
    
