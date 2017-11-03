#!/usr/bin/env python
'''
Follow up for "Unique Paths":

Now consider if some obstacles are added to the grids. How many unique paths would there be?

An obstacle and empty space is marked as 1 and 0 respectively in the grid.

For example,
There is one obstacle in the middle of a 3x3 grid as illustrated below.

[
  [0,0,0],
  [0,1,0],
  [0,0,0]
]
The total number of unique paths is 2.
'''

def uniquePathsWithObstacles(obstacleGrid):

    if not obstacleGrid:
	return 0


    nrows = len(obstacleGrid)
    ncols = len(obstacleGrid[0])

   
    # if starting element is an obstacle, 0 paths
    if obstacleGrid[0][0] == 1:
	    return 0


    a = [[0] * ncols for i in range(nrows)]
    
    # since we need a starting point. Also  # ways to reach starting point is 1
    a[0][0] = 1


  
    # for first row and first col, 
    # if current element is 0, then # paths to it = # paths to the prev element  
    for i in range(1, ncols):
	    if obstacleGrid[0][i] != 1:
	        a[0][i] = a[0][i - 1]

       
    for i in range(1, nrows):
	    if obstacleGrid[i][0] != 1:
	        a[i][0] = a[i - 1][0]

       
    for i in range(1, nrows):
	    for j in range(1, ncols):
	        if obstacleGrid[i][j] != 1:
	            a[i][j] = a[i][j - 1] + a[i - 1][j]

    return a[-1][-1]



def uniquePathsWithObstacles_2(obstacleGrid):

        if not obstacleGrid:
            return 0


        nrows = len(obstacleGrid)
        ncols = len(obstacleGrid[0])


        if obstacleGrid[0][0] == 1:
            return 0


        a = [0] * ncols
        a[0] = 1


        for i in range(nrows):
            for j in range(ncols):
                if obstacleGrid[i][j] != 1 and j > 0:
                    a[j] = a[j] + a[j -1]

                elif obstacleGrid[i][j] == 1:
                    a[j] = 0

        return a[-1]  




if __name__ == '__main__':
    print uniquePathsWithObstacles_2([[0]])
