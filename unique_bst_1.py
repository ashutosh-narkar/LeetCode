#!/usr/bin/env python
'''
Given n, how many structurally unique BST's (binary search trees) that store values 1...n?

For example,
Given n = 3, there are a total of 5 unique BST's.

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3

Solution:

For each sequence from 1 to n, # of BSTs equals:
Sum of BSTs where each number (from 1 to n) is considered as the root node

For each node, # of BSTs equals:
Product of the number of BST for its left and right subtrees.


Denote bst[i] = the number of BSTs can be constructed that store values from 1..n.

'''
def numTrees(n):

    if n <= 1:
	return 1


    res = [0] * (n + 1)

    res[0] = 1  # for zero nodes  we can have 1 bst of null
    res[1] = 1
    res[2] = 2

    for i in range(3, n + 1):
	    for j in range(1, i + 1):
	        res[i] +=  res[j - 1] * res[i - j]   # left subtree * right subtree 

    return res[-1]

