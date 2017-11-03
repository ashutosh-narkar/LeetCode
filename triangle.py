#!/usr/bin/env python
'''
Given a triangle, find the minimum path sum from top to bottom. Each step you may move to adjacent numbers on the row below.

For example, given the following triangle

[
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]

The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11).

Solution:
'Bottom-up' DP: we start from the nodes on the bottom row; the min pathsums for these nodes are the values of the nodes themselves. 
From there, the min pathsum at the ith node on the kth row would be the lesser of the pathsums of its two children plus the value of itself, i.e.:

minpath[k][i] = min( minpath[k+1][i], minpath[k+1][i+1]) + triangle[k][i];


Or even better, since the row minpath[k+1] would be useless after minpath[k] is computed, 
we can simply set minpath as a 1D array, and iteratively update itself:

For the kth level:
minpath[i] = min( minpath[i], minpath[i+1]) + triangle[k][i];

'''
def minTotal(triangle):
    if not triangle:
        return 

    result = triangle[-1]

    # for every layer except last one
    for layer in reversed(range(len(triangle) - 1)):
        # check its every node
        for i in range(layer + 1):
            # Find the lesser of its two children, and sum the current value in the triangle with it.
            result[i] = min(result[i], result[i + 1]) + triangle[layer][i]

    return result[0]

if __name__ == '__main__':
    data = [[2],
            [3,4],
            [6,5,7],
            [4,1,8,3]
           ]

    print 'Min path sum is {}'.format(minTotal(data))
