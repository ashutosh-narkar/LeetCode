#!/usr/bin/env python
'''
Max points on a line
Given n points on a 2D plane, find the maximum number of points that lie on the same straight line.

http://yucoding.blogspot.com/2013/12/leetcode-question-max-points-on-line.html

'''
# Definition for a point
class Point:

    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b


def maxPoints(points):
    '''
    @param points, a list of Points
    '''

    if len(points) < 2:
        return len(points)

    
    m = 0 #result value
    for i in range(len(points)):

        l = {}  #every time reset the dict    
        duplicates = 1
        for j in range(len(points)):
       
            # dulpicate points
            if i != j and points[i].x == points[j].x and points[i].y == points[j].y:
                duplicates += 1


            elif i != j:

                # vertical line
                if points[i].x == points[j].x:
                    l['v'] = l.get('v', 0) + 1

                # horizontal line
                elif points[i].y == points[j].y:
                    l['h'] = l.get('h', 0) + 1

                # regular slope
                else:
                    slope = (points[i].y-points[j].y)/float(points[i].x-points[j].x)
                    l[slope] = l.get('slope', 0) + 1

        if l:
            m = max(m, max(l.values()) + duplicates)
        else: #if all points are duplicates, l is empty.
            m = max(m, duplicates)
                    
    return m                
