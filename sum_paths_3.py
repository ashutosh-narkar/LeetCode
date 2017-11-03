#!/usr/bin/env python
'''
Given a binary tree, find the maximum path sum.
The path may start and end at any node in the tree.

For ex.

     1
   /   \
  2     3

Return 6

This is basically post order traversal

'''
#Definition for a  binary tree node

max_val = 0

class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None


def maxPathSum(root):

    findmax(root)
    return max_val


def findmax(node):
    if not node:
        return 0

    # recursively get sum of left and right path
    left = max(0, findmax(node.left))
    right = max(0, findmax(node.right))

    # update maximum here
    global max_val
    max_val = max(max_val, left + right + node.val)
 
    # return sum of largest path of current node 
    return node.val + max(left, right)

if __name__ == '__main__':

    root = TreeNode(1)
    node1 = TreeNode(2)
    node2 = TreeNode(3)

    root.left = node1
    root.right = node2

    print maxPathSum(root)
