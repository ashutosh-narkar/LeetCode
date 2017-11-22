#!/usr/bin/env python
"""
You are given a m x n 2D grid initialized with these three possible values.
-1 - A wall or an obstacle.
0 - A gate.
INF - Infinity means an empty room.

Fill each empty room with the distance to its nearest gate.
If it is impossible to reach a gate, it should be filled with INF.

For example, given the 2D grid:
INF  -1  0  INF
INF INF INF  -1
INF  -1 INF  -1
  0  -1 INF INF

After running your function, the 2D grid should be:
  3  -1   0   1
  2   2   1  -1
  1  -1   2  -1
  0  -1   3   4

Solution: Start DFS from each gate(0) and then check neighbours

Similar logic to word_search_1.py
"""


def walls_and_gates(rooms):
    if not rooms:
        return []

    rows = len(rooms)
    cols = len(rooms[0])

    for i in range(rows):
        for j in range(cols):
            if rooms[i][j] == 0:
                dfs(rooms, 0, i, j)


def dfs(rooms, distance, row, col):

    # invalid rows
    if row < 0 or row >= len(rooms):
        return

    # invalid columns
    if col < 0 or col >= len(rooms[0]):
        return

    # Is wall?
    if rooms[row][col] == -1:
        return

    # Distance greater than current
    if distance > rooms[row][col]:
        return

    rooms[row][col] = distance

    # go up, down, left, right
    dfs(rooms, distance + 1, row - 1, col)
    dfs(rooms, distance + 1, row + 1, col)
    dfs(rooms, distance + 1, row, col - 1)
    dfs(rooms, distance + 1, row, col + 1)

if __name__ == '__main__':
    rooms = [[float('inf'), -1, 0, float('inf')],
             [float('inf'), float('inf'), float('inf'), -1],
             [float('inf'), -1, float('inf'), -1],
             [0, -1, float('inf'), float('inf')]]

    walls_and_gates(rooms)

    print rooms
