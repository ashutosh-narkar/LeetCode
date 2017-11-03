#!/usr/bin/env python
'''
In a maze with empty spaces and walls, given a starting point and ending point, find a path.
'''
from collections import deque

def explore(maze, start_row, start_col, end_row, end_col):
    
    if not maze:
        return

    visited = []
    visited.append((start_row, start_col))

    queue = deque()
    queue.append((start_row, start_col))

    pred = {}
    pred[(start_row, start_col)] = None


    while queue:
        row, col = queue.popleft()

        # reached end. This condition is not necessary but results in early exit
        if row == end_row  and col == end_col:
            break

        # next row
        if isFree(maze, row + 1, col) and (row + 1, col) not in visited:
            visited.append((row + 1, col))
            queue.append((row + 1, col))
            pred[(row + 1, col)] = (row, col)
  
        # prev row
        if isFree(maze, row - 1, col) and (row - 1, col) not in visited:
            visited.append((row - 1, col))
            queue.append((row - 1, col))
            pred[(row - 1, col)] = (row, col)

    
        # prev col
        if isFree(maze, row, col - 1) and (row, col - 1) not in visited:
            visited.append((row, col - 1))
            queue.append((row, col - 1))
            pred[(row, col - 1)] = (row, col)


        # next col
        if isFree(maze, row, col + 1) and (row, col  + 1) not in visited:
            visited.append((row, col + 1))
            queue.append((row, col + 1))
            pred[(row, col + 1)] = (row, col)


    return pred, visited 



def isFree(maze, row, col):
    '''
    return if this is a valid location
    valid location -> any location within the maze that's not an wall (ie.5)
    '''
    if 0 <= row < len(maze) and 0 <= col < len(maze[0]) and maze[row][col] == 0:
        return True
    return False


def findPath(preds, start_row, start_col, end_row, end_col):

    row = end_row
    col = end_col

    result = []
    
    while(preds[(row, col)]):
        result.append((row, col))
        row, col = preds[(row, col)]


    # add the start position
    result.append((start_row, start_col))
    result.reverse()
    return result


def mazeSolver():
    maze = [[0, 0, 0, 0],
            [5, 0, 0, 5],
            [0, 0, 0, 0],
            [0, 5, 0, 0]]

    # in the maze '0' indicates a space, '5' indicates the wall
 
    parents, visited = explore(maze, 0, 1, 3, 2)


    if (3, 2) in visited:
        print 'End position Can be reached'
        path  = findPath(parents, 0, 1, 3, 2)
        print path

    else:
        print 'End position cannot be reached'


if __name__ == '__main__':
    mazeSolver()
