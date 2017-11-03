#!/usr/bin/env python
'''
A city's skyline is the outer contour of the silhouette formed by all the buildings in that city
when viewed from a distance.

For diagram of buildings: https://leetcode.com/problems/the-skyline-problem/description/

The geometric information of each building is represented by a triplet of integers [Li, Ri, Hi],
where Li and Ri are the x coordinates of the left and right edge of the ith building, respectively,
and Hi is its height.

It is guaranteed that 0 <= Li, Ri <= INT_MAX, 0 < Hi <= INT_MAX, and Ri - Li > 0.

You may assume all buildings are perfect rectangles grounded on an absolutely flat surface at height 0.

The output is a list of "key points" in the format of [ [x1,y1], [x2, y2], [x3, y3], ... ]
that uniquely defines a skyline.

Notes:

The number of buildings in any input list is guaranteed to be in the range [0, 10000].
The input list is already sorted in ascending order by the left x position Li.
The output list must be sorted by the x position.
There must be no consecutive horizontal lines of equal height in the output skyline.
For instance, [...[2 3], [4 5], [7 5], [11 5], [12 7]...] is not acceptable;
the three lines of height 5 should be merged into one in the final output as such: [...[2 3], [4 5], [12 7], ...]


Solution:
1) Maintain a MAX heap where each element is a tuple of form (height, end_coordinate).
This means the tallest building will be at the top of the heap. If 2 building have same height,
then the one with the larger end co-ordinate will appear first

2) The idea is to do line sweep and just process the buildings only at the start and end points.

3) If the current building's start co-ordinate <= tallest building's end co-ordinate (ie overlap),
we push the current building on the heap. In fact push all those buildings that start at the same co-ordinate
as the current building

4) If the current building's start co-ordinate > tallest building's end co-ordinate (ie NO overlap),
keep popping the heap either till it get empty or till we find a building whose end co-ordinate is more than
that of the tallest building

5) If the current maximum height in the heap differs from the last in the skyline, we add it to the skyline.

Runtime: O(n logn)
'''

from heapq import *

def get_skyline(buildings):
    """
    :type buildings: List[List[int]]
    :rtype: List[List[int]]
    """
    if not buildings:
        return []

    skyline = []
    heap = []
    i = 0
    n = len(buildings)

    # There could be a case where i > n but heap still has buildings
    while i < n or heap:

        # Overlap case
        if not heap or (i < n and buildings[i][0] <= -heap[0][1]):
            x = buildings[i][0]       # current building's start co-ordinate
            while i < n and buildings[i][0] == x:
                heappush(heap, (-buildings[i][2], -buildings[i][1]))    # we push with -ve signs since we want max heap

                i += 1

        # Non-overlap case
        else:
            x = -heap[0][1]     # tallest building's end co-ordinate
            while heap and -heap[0][1] <= x:
                heappop(heap)

        height = 0 if not heap else -heap[0][0]

        # update skyline
        if not skyline or skyline[-1][1] != height:
            skyline.append([x, height])

    return skyline
