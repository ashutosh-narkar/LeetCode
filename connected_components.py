#!/usr/bin/env python
'''
Given n nodes labeled from 0 to n - 1 and a list of undirected edges (each edge is a pair of nodes),
write a function to find the number of connected components in an undirected graph.

Example 1:
     0          3
     |          |
     1 --- 2    4

Given n = 5 and edges = [[0, 1], [1, 2], [3, 4]], return 2.


Example 2:
     0           4
     |           |
     1 --- 2 --- 3
Given n = 5 and edges = [[0, 1], [1, 2], [2, 3], [3, 4]], return 1.

Note:
You can assume that no duplicate edges will appear in edges.
Since all edges are undirected, [0, 1] is the same as [1, 0] and thus will not appear together in edges

Solution: Union-Find algorithm
Runtime: O(m log n) where m is # edges and n is # nodes

'''


def count_components(n, edges):

    # initialize n isolated islands
    # Initially, all slots of parent array are initialized to - 1(means there is only one item in every subset)

    nums = [-1] * n

    # assume every node is connected to only itself
    count = n

    for edge in edges:
        x = find(nums, edge[0])
        y = find(nums, edge[1])

        # nodes are in different subsets
        if x != y:
            count -= 1

            # union the nodes
            nums[x] = y

    return count


# For find operation use PATH COMPRESSION.
# In this technique, make every other node in the path point to its grand-parent.
# This keeps the tree almost flat !
# Hence runtime for find is O(logn)

def find(nums, i):

    # node is in it's own subset if nums[i] == -1
    while nums[i] != -1:
        nums[i] = nums[nums[i]]   # path compression by halving
        i = nums[i]

    return i

if __name__ == '__main__':
    n = 5

    edges = [[0, 1], [1, 2], [3, 4]]
    assert count_components(n, edges) == 2

    edges = [[0, 1], [1, 2], [2, 3], [3, 4]]
    assert count_components(n, edges) == 1

    print "Tests passed"
