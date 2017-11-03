#!/usr/bin/env python
'''
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. 
The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

How many possible unique paths are there?

Solution 1:
From the description we know that, the robot can only move down or right, which means, if the robot is now in position (x,y), 
then the position before this step must be  either (x-1,y) or (x, y-1). 
Since current position is only from these two previous positions, 
the number of possible paths that the robot can reach this current position (x,y) is the SUM of paths from (x-1, y) and (x, y-1).


Note that the boundary of the map, we can easily know that the top row and the first column of the map are all 1s.

Runtime = O(m + n) 
Space = O(m + n)


Solution 2:
We only need to store the previous row/column to perform the calculation for the next one. 
So an 1-d array would suffice. You could also choose to iterate through m or n depending on which direction you choose to go (by row or by column). 
Note that the first element of the array will always be 1.

Runtime = O(m + n) 
Space = O(n) or O(m)
'''

def uniquePaths(m, n):

    if not (m and n):
	    return 0

	
    # Note : we are creating a grid of size m X n and NOT (m + 1) X (n + 1)
    a = [[0] * n for i in range(m)]


    # boundary elements are all 1. Since # ways to reach an element in the top row and first col is 1 
    for i in range(n):
	    a[0][i] = 1
	

    for i in range(m):
	    a[i][0] = 1

	

    for i in range(1, m):
	    for j in range(1, n):
	        a[i][j] = a[i][j -1] + a[i - 1][j]

    return a[m - 1][n - 1]


def uniquePaths_2(m, n):

        if not (m and n):
            return 0
            

        # set the first row
        # boundary elements are all 1. Since # ways to reach an element in the top row and/or first col is 1
        a = [1] * n

        # iterate ror by row
        for i in range(1, m):
           for j in range(1, n):
               a[j] = a[j] + a[j - 1]           #  current val =  val of element in same col prev row (this happens to be current val itself)  + val of element in same row prev col

        return a[-1]




