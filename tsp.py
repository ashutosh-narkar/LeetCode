#!/usr/bin/env python
"""
Description + DP solution: https://people.eecs.berkeley.edu/~vazirani/algorithms/chap6.pdf
Runtime Brute Force: O(n!)
Runtime DP: O(n^2 * 2^n). There are n * 2^n sub-problems and each takes linear time to solve

Given a list of cities and the distances between them, what is the shortest possible path that visits each city
exactly once and returns to the origin city?

"""
import math

def distance(point1, point2):
    """
    Returns the Euclidean distance of two points in the Cartesian Plane.

    >>> distance([3,4],[0,0])
    5.0
    >>> distance([3,6],[10,6])
    7.0
    """
    return math.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)


def total_distance(points):
    """
    Returns the length of the path passing through
    all the points in the given order.

    >>> total_distance([[1,2],[4,6]])
    5.0
    >>> total_distance([[3,6],[7,6],[12,6]])
    9.0
    """
    return sum([distance(point, points[index + 1]) for index, point in enumerate(points[:-1])])


def travelling_salesman_heuristic(points, start=None):
    """
    TSP solution using a heuristic - always go to the nearest city
    """
    if start is None:
        start = points[0]
    must_visit = points
    path = [start]
    must_visit.remove(start)
    while must_visit:
        nearest = min(must_visit, key=lambda x: distance(path[-1], x))
        path.append(nearest)
        must_visit.remove(nearest)
    return path


if __name__ == '__main__':
    points = [[0, 0], [1, 5.7], [2, 3], [3, 7],
              [0.5, 9], [3, 5], [9, 1], [10, 5]]

    print total_distance(travelling_salesman_heuristic(points))