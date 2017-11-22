#!/usr/bin/env python
"""
For a undirected graph with tree characteristics, we can choose any node as the root.
The result graph is then a rooted tree. Among all possible rooted trees, those with minimum height are called
minimum height trees (MHTs). Given such a graph, write a function to find all the MHTs
and return a list of their root labels.

Format
The graph contains n nodes which are labeled from 0 to n - 1. You will be given the number n
and a list of undirected edges (each edge is a pair of labels).

You can assume that no duplicate edges will appear in edges. Since all edges are undirected,
[0, 1] is the same as [1, 0] and thus will not appear together in edges.

Example 1:

Given n = 4, edges = [[1, 0], [1, 2], [1, 3]]

        0
        |
        1
       / \
      2   3
return [1]

Example 2:

Given n = 6, edges = [[0, 3], [1, 3], [2, 3], [4, 3], [5, 4]]

     0  1  2
      \ | /
        3
        |
        4
        |
        5
return [3, 4]

Note:

(1) According to the definition of tree on Wikipedia: "a tree is an undirected graph in which any two vertices
are connected by exactly one path. In other words, any connected graph without simple cycles is a tree."

(2) The height of a rooted tree is the number of edges on the longest downward path between the root and a leaf.

Solution: https://discuss.leetcode.com/topic/30572/share-some-thoughts
We start from every end, by end we mean vertex of degree 1 (aka leaves).
We let the pointers move the same speed. When two pointers meet, we keep only one of them,
until the last two pointers meet or one step away we then find the roots.

It is easy to see that the last two pointers are from the two ends of the longest path in the graph.

The actual implementation is similar to the BFS topological sort. Remove the leaves, update the degrees of
inner vertexes. Then remove the new leaves. Doing so level by level until there are 2 or 1 nodes left.
What's left is our answer!

The time complexity and space complexity are both O(n).

Note that for a tree we always have V = n, E = n-1.
"""


def find_min_height_trees(n, edges):
    """
    :type n: int
    :type edges: List[List[int]]
    :rtype: List[int]
    """
    if n == 0:
        return []

    if n == 1:
        return [0]

    # create adjacency list representation of the graph
    # we use a set instead of a list as we want O(1) removal
    graph = [set() for _ in range(n)]

    for i, j in edges:
        graph[i].add(j)
        graph[j].add(i)

    # leaf nodes to start the traversal
    leaves = [i for i in range(n) if len(graph[i]) == 1]

    while n > 2:
        n -= len(leaves)
        newLeaves = []

        for leaf in leaves:
            node = graph[leaf].pop()
            graph[node].remove(leaf)

            # check if leaf
            if len(graph[node]) == 1:
                newLeaves.append(node)

        leaves = newLeaves

    return leaves
