#!/usr/bin/env python
"""
You want to build a house on an empty land which reaches all buildings in the shortest amount of distance.
You can only move up, down, left and right. You are given a 2D grid of values 0, 1 or 2, where:

Each 0 marks an empty land which you can pass by freely.

Each 1 marks a building which you cannot pass through.

Each 2 marks an obstacle which you cannot pass through.

For example, given three buildings at (0,0), (0,4), (2,2), and an obstacle at (0,2):
1 - 0 - 2 - 0 - 1
|   |   |   |   |
0 - 0 - 0 - 0 - 0
|   |   |   |   |
0 - 0 - 1 - 0 - 0
The point (1,2) is an ideal empty land to build a house, as the total travel distance of 3+3+1=7 is minimal.
So return 7.

Solution: A BFS problem. Search from each building and calculate the distance to the building.
One thing to note is an empty land must be reachable by all buildings.

***** Similar to knight_target.py *****

"""
from collections import deque


def shortest_distance(grid):
    if not grid:
        return 0

    rows = len(grid)
    cols = len(grid[0])

    # sum of the shortest distance of the empty land from all reachable buildings
    distance = [[0] * cols for _ in range(rows)]

    # number of buildings reachable from empty land
    reach = [[0] * cols for _ in range(rows)]

    # count total buildings
    num_buildings = 0

    # Find the minimum distance from all buildings
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                num_buildings += 1
                bfs(grid, i, j, distance, reach)

    result = float('inf')

    # check the min distance reachable from land to all buildings
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 0 and reach[i][j] == num_buildings:
                result = min(result, distance[i][j])

    if result == float('inf'):
        return -1

    return result


def bfs(grid, row, col, distance, reach):

    # 4 positions we can travel
    # '-' indicates up and left direction
    # '+' indicates down and right direction
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    q = deque()
    q.append((row, col, 0))        # push the building cell with 0 distance

    rows = len(grid)
    cols = len(grid[0])

    visited = [[False] * cols for _ in range(rows)]
    visited[row][col] = True

    while q:
        i, j, dist = q.popleft()

        # check for empty land
        if grid[i][j] == 0:
            reach[i][j] += 1
            distance[i][j] += dist

        for x in range(4):
            next_row = i + dx[x]
            next_col = j + dy[x]

            # check valid row/col
            # We cannot pass through buildings and obstacles
            if 0 <= next_row < rows and 0 <= next_col < cols and grid[next_row][next_col] == 0 \
                and not visited[next_row][next_col]:
                visited[next_row][next_col] = True
                q.append((next_row, next_col, dist + 1))


if __name__ == '__main__':
    grid = [[1, 0, 2, 0, 1],
            [0, 0, 0, 0, 0],
            [0, 0, 1, 0, 0]]

    print shortest_distance(grid)
