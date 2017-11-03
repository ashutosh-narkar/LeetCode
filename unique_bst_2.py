#!/usr/bin/env python
'''
Given n, generate all structurally unique BST's (binary search trees) that store values 1...n.

For example,
Given n = 3, your program should return all 5 unique BST's shown below.

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3


Solution: "Return All" suggests the use of DFS

Set the root from the start position to the end position, 
and recursively construct the left subtree with the left part 
and the right subtree with the right part.

Then construct the current node, and push it to the current solution vector.

time complexity if O(2^n)
'''

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None



# @return a list of tree node
def generateTrees(n):


    if not n or n < 1:
	return [None]


    result = []
    dfs(1, n, result)
    return result

        

def dfs(start, end, result):

    if start > end:
        result.append(None)             # generate a null node
        return


    for i in range(start, end + 1):     # "end + 1" since we have to include the nth node
        left = []
        dfs(start, i - 1, left)         # generate left subtree 

        right = []
        dfs(i + 1, end, right)          # generate right subtree 

        
        # create node i and store tree rooted at node i
        for x in range(len(left)):
            for y in range(len(right)):
                node = TreeNode(i)
                node.left = left[x]
                node.right = right[y]
                result.append(node)



