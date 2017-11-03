#!/usr/bin/env python
'''
Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. 

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. 
You may assume all four edges of the grid are all surrounded by water.

Example 1:

11110
11010
11000
00000
Answer: 1

Example 2:

11000
11000
00100
00011
Answer: 3


'''

# Solution 1: Using DFS. The basic idea of the following solution is merging adjacent lands,
# and the merging should be done recursively.
# Each element is visited once only. So time is O(m * n).

'''
Solution Explanation:
This is an variation of the standard problem: 
“Counting number of connected components in a undirected graph”.

A connected component of an undirected graph is a subgraph in which every two vertices are 
connected to each other by a path(s), and which is connected to no other vertices outside the subgraph.

A graph where all vertices are connected with each other, has exactly one connected component,
consisting of the whole graph. Such graph with only one connected component is called as Strongly Connected Graph.

The problem can be easily solved by applying DFS() on each component. 
In each DFS() call, a component or a sub-graph is visited. We will call DFS on the next un-visited component. 
The number of calls to DFS() gives the number of connected components. BFS can also be used.
'''


def numIslands(grid):
    """
    :type grid: List[List[str]]
    :rtype: int
    """

    if not grid:
        return 0

    count = 0

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == "1":
                dfs(grid, i, j)
                count += 1

    return count


def dfs(grid, i, j):
    if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] != "1":
        return

    grid[i][j] = "#"
    dfs(grid, i - 1, j)
    dfs(grid, i + 1, j)
    dfs(grid, i, j - 1)
    dfs(grid, i, j + 1)


# Solution 2: BFS

from collections import deque


def numIslands(grid):

    if not grid:
        return 0
        

    lands = set()

    nrows = len(grid)
    ncols = len(grid[0])

    
    # get all the land positions. We will use bfs on these locations
    for i in range(nrows):
        for j in range(ncols):
            if grid[i][j] == '1':
                lands.add((i, j))

                

    count = 0
    while lands:

        # start of an island
        row, col = lands.pop()

        count += 1 

        

        queue = deque()
        queue.append((row, col))

        # finding the complete island
        while queue:

            i, j = queue.popleft()

            # up
            if (i - 1, j) in lands:
                queue.append(( i - 1, j))
                lands.remove((i - 1, j))

            # down
            if (i + 1, j) in lands:
                queue.append(( i + 1, j))
                lands.remove((i + 1, j))

                
            # left
            if (i, j - 1) in lands:
                queue.append(( i, j - 1))
                lands.remove((i, j - 1))

               
            # right
            if (i, j + 1) in lands:
                queue.append(( i, j + 1))
                lands.remove((i, j + 1))
                

    return count

