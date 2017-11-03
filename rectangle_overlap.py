#!/usr/bin/env python
'''
Find if the given two rectangles overlap or not.

Note that a rectangle can be represented by two coordinates, 
top left and bottom right. So mainly we are given following four coordinates.

l1: Top Left coordinate of first rectangle.
r1: Bottom Right coordinate of first rectangle.
l2: Top Left coordinate of second rectangle.
r2: Bottom Right coordinate of second rectangle.

Two rectangles DO NOT overlap if one of the following conditions is true.
1) One rectangle is above top edge of other rectangle.
2) One rectangle is on left side of left edge of other rectangle.

  l1______________   l2 ________________
  |              |   |                  |
  |              |   |                  |
  |              |   |                  |
  |______________r1  |__________________r2
'''

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def doOverlap(l1, r1, l2, r2):

    # If one rectangle is above other
    if r1.y > l2.y or r2.y > l1.y:
        return False

    # If one rectangle is on left side of other
    if r1.x < l2.x or r2.x < l1.x:
        return False

    return True


if __name__ == '__main__':

    l1 = Point(0, 10)
    r1 = Point(10, 0)
    l2 = Point(5, 5)
    r2 = Point(15, 0)

    if doOverlap(l1, r1, l2, r2):
        print 'Rectangles overlap'

    else:
        print 'Rectangles do not overlap'
    
