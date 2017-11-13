#!/usr/bin/python
"""
Given a 2D screen, location of a pixel in the screen and a color,
replace color of the given pixel and all adjacent same colored pixels with the given color.

Example:
    Input:

    screen[M][N] =    {{1, 1, 1, 1, 1, 1, 1, 1},
                      {1, 1, 1, 1, 1, 1, 0, 0},
                      {1, 0, 0, 1, 1, 0, 1, 1},
                      {1, 2, 2, 2, 2, 0, 1, 0},
                      {1, 1, 1, 2, 2, 0, 1, 0},
                      {1, 1, 1, 2, 2, 2, 2, 0},
                      {1, 1, 1, 1, 1, 2, 1, 1},
                      {1, 1, 1, 1, 1, 2, 2, 1},
                      };
    x = 4, y = 4, newColor = 3

    Output:

    screen[M][N] =    {{1, 1, 1, 1, 1, 1, 1, 1},
                      {1, 1, 1, 1, 1, 1, 0, 0},
                      {1, 0, 0, 1, 1, 0, 1, 1},
                      {1, 3, 3, 3, 3, 0, 1, 0},
                      {1, 1, 1, 3, 3, 0, 1, 0},
                      {1, 1, 1, 3, 3, 3, 3, 0},
                      {1, 1, 1, 1, 1, 3, 1, 1},
                      {1, 1, 1, 1, 1, 3, 3, 1},
                      };

Solution: DFS
"""


def flood_fill(screen, row, col, newColor):
    if not screen:
        return

    oldColor = screen[row][col]

    dfs(screen, row, col, oldColor, newColor)
    return screen


def dfs(screen, row, col, oldColor, newColor):

    # invalid rows
    if row < 0 or row >= len(screen):
        return

    # invalid columns
    if col < 0 or col >= len(screen[0]):
        return

    if screen[row][col] != oldColor:
        return

    # replace the color
    screen[row][col] = newColor

    # go left, right, up and down
    dfs(screen, row, col - 1, oldColor, newColor)
    dfs(screen, row, col + 1, oldColor, newColor)
    dfs(screen, row - 1, col, oldColor, newColor)
    dfs(screen, row + 1, col, oldColor, newColor)

if __name__ == '__main__':
    screen = [[1, 1, 1, 1, 1, 1, 1, 1],
              [1, 1, 1, 1, 1, 1, 0, 0],
              [1, 0, 0, 1, 1, 0, 1, 1],
              [1, 2, 2, 2, 2, 0, 1, 0],
              [1, 1, 1, 2, 2, 0, 1, 0],
              [1, 1, 1, 2, 2, 2, 2, 0],
              [1, 1, 1, 1, 1, 2, 1, 1],
              [1, 1, 1, 1, 1, 2, 2, 1]]

    row = 4
    col = 4
    newColor = 3
    result = flood_fill(screen, row, col, newColor)
    for item in result:
        print item