'''
Given set of n points (Xi, Yi), write a function to find k nearest points from origin.

Runtime - O(nlogk)
'''

import math
from heapq import heappush, heappop

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def find_nearest_k(points, k):
    
    # compute the euclidian dist of all points from given point. In this case origin
    dist = []

    for point in points:
        edist = math.sqrt(point.x ** 2 + point.y ** 2)
        dist.append(edist)

    # build a max heap from k elements in array
    # the heap is organized as a list of tuples (dist, point)
    # since we maintain a max heap, we negate the dist before pushing
    h = []
    for i in range(k):
        heappush(h, (-dist[i], points[i]))

    # the remaining points
    for i in range(k, len(dist)):
        if dist[i] >= -h[0][0]:
            continue
        
        else:
            heappop(h)
            heappush(h, (-dist[i], points[i]))

    # heap will contain 'k' nearest points
    return h


if __name__ == '__main__':

    p0 = Point(0,0)
    p1 = Point(1,1)
    p2 = Point(2,2)
    p3 = Point(3,3)
    p4 = Point(4,4)
    p5 = Point(5,5)
    p = [p0, p1, p2, p3, p4, p5]

    res = find_nearest_k(p, 3)
  
    for item in res:
        item = item[1]
        print 'x:{}  y:{}'.format(item.x, item.y) 
