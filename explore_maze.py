#!/usr/bin/env python
'''
Exploring a Maze (http://interactivepython.org/runestone/static/pythonds/Recursion/ExploringaMaze.html)
'''

import os
FILE_PATH = os.path.expanduser('~/misc/maze.txt')

class Maze:

    def __init__(self, mazeFileName):
        self.numRows, self.numCols = 0, 0
        self.mazeList = []
        self.startRow, self.startCol = 0, 0

        with open(mazeFileName, 'r') as f:
            lines = f.readlines()
            for i in range(len(lines)):
                line = list(lines[i].rstrip())  # remove '/n' at end of line
                self.mazeList.append(line)
                # check the starting point
                if 'S' in line:
                    self.startRow, self.startCol = i, line.index('S')

        self.numRows = len(self.mazeList)
  	self.numCols = len(self.mazeList[0])


    def updatePosition(self, row, col, val):
        self.mazeList[row][col] = val

    def isExit(self, row, col):
        return(row == 0 or
               row == self.numRows - 1 or
               col == 0 or
               col == self.numCols - 1)

    def __getitem__(self, idx):
        return self.mazeList[idx]


def searchFrom(maze, row, col):
    #  1. We have run into an obstacle, return false
    if maze[row][col] == '+':
        return False

    #  2. We have found a square that has already been explored
    elif maze[row][col] in ('.', '-'):
        return False

    # 3. We have found an outside edge not occupied by an obstacle
    elif maze.isExit(row, col):
        return True

    # 4. We met a dead end
   # elif maze[row][col] == '-':
   #     return False
    
    # mark the position as visited
    maze.updatePosition(row, col, '.')
    
    # short circuiting to try other directions
    found = searchFrom(maze, row+1, col) or \
            searchFrom(maze, row-1, col) or \
            searchFrom(maze, row, col+1) or \
            searchFrom(maze, row, col-1)
    if found:
        maze.updatePosition(row, col, '0') # found the maze exit
    else:
        maze.updatePosition(row, col, '-') # found a dead end
    return found

if __name__ == '__main__':
    maze = Maze(FILE_PATH)
    res = searchFrom(maze, maze.startRow, maze.startCol)
    
    if res:
        print 'Found exit to maze'
    else:
        print 'No exit to maze found'









