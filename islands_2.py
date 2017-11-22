#!/usr/bin/env python
"""
You are given a map in form of a two-dimensional integer grid where 1 represents land and 0 represents water.
Grid cells are connected horizontally/vertically (not diagonally).
The grid is completely surrounded by water, and there is exactly one island (i.e., one or more connected land cells).
The island doesn't have "lakes" (water inside that isn't connected to the water around the island).
One cell is a square with side length 1. The grid is rectangular, width and height don't exceed 100.

Determine the perimeter of the island.

SEE https://leetcode.com/problems/island-perimeter/description/ for picture


Solution:
1) Find an island and add 4 to result
2) If the island has a neighbour on its left, subtract 2 from result
3) If the island has a neighbour above it, subtract 2 from result

This is because when two islands merge, 2 sides get eliminated

+--+     +--+                   +--+--+
|  |  +  |  |          ->       |     |
+--+     +--+                   +--+--+
"""


def islandPerimeter(grid):
    """
    :type grid: List[List[int]]
    :rtype: int
    """

    if not grid:
        return 0

    result = 0

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 1:
                result += 4

                # if neighbour on left
                if j > 0 and grid[i][j - 1] == 1:
                    result -= 2

                # if neighbour on top:
                if i > 0 and grid[i - 1][j] == 1:
                    result -= 2

    return result
