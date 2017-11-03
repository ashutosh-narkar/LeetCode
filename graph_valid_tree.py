#!/usr/bin/env python
'''
Given n nodes labeled from 0 to n - 1 and a list of undirected edges (each edge is a pair of nodes),
check if these edges form a valid tree.


Logic:
To tell whether a graph is a valid tree, we have to:

1) Make sure there is no cycle in the graph - this has to be a none-cyclic graph;
2) Make sure every node is reached - this has to be a connected graph


Solution: Union-Find algorithm
http://www.geeksforgeeks.org/union-find/
https://www.cs.princeton.edu/~rs/AlgsDS07/01UnionFind.pdf

Find: Determine which subset a particular element is in.
This can be used for determining if two elements are in the same subset.

Union: Join two subsets into a single subset.

Runtime: O(m log n) where m is # edges and n is # nodes
'''

def valid_tree(n, edges):

    # initialize n isolated islands
    # Initially, all slots of parent array are initialized to - 1(means there is only one item in every subset)

    nums = [-1] * n

    for edge in edges:
        x = find(nums, edge[0])
        y = find(nums, edge[1])

        # if two vertices happen to be in the same subset
        # then there is a cycle
        if x == y:
            return False

        # if the nodes are in different subsets, union them
        nums[x] = y

    # for a connected graph, # edges = number of nodes - 1
    return len(edges) == n - 1


# For find operation use PATH COMPRESSION.
# In this technique, make every other node in the path point to its grand-parent.
# This keeps the tree almost flat !
# Hence runtime for find is O(logn)

def find(nums, i):

    # node is in it's own subset if nums[i] == -1
    while nums[i] != -1:
        nums[i] = nums[nums[i]]     # path compression by halving
        i = nums[i]

    return i


if __name__ == '__main__':
    n = 5

    edges = [[0, 1], [0, 2], [0, 3], [1, 4]]
    assert valid_tree(n, edges) == True

    edges = [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]
    assert valid_tree(n, edges) == False

    print "Tests passed"
