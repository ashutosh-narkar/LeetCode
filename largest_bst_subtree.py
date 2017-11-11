#!/usr/bin/env python
"""
Given a Binary Tree, write a function that returns the size of the largest subtree
which is also a Binary Search Tree (BST). If the complete Binary Tree is BST, then return the size of whole tree.

Input:
      5
    /  \
   2    4
 /  \
1    3

Output: 3
The following subtree is the
maximum size BST subtree
   2
 /  \
1    3


Input:
       50
     /    \
  30       60
 /  \     /  \
5   20   45    70
              /  \
            65    80
Output: 5
The following subtree is the
maximum size BST subtree
      60
     /  \
   45    70
        /  \
      65    80



"""
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class SubTree(object):
    def __init__(self, largest, n, min, max):
        self.largest = largest                 # largest BST
        self.n = n                             # number of nodes in this ST
        self.min = min                         # min val in this ST
        self.max = max                         # max val in this ST


def largestBSTSubtree(root):
        res = dfs(root)
        return res.largest


def dfs(root):
    if not root:
        return SubTree(0, 0, float('inf'), float('-inf'))

    left = dfs(root.left)
    right = dfs(root.right)

    if root.val > left.max and root.val < right.min:  # valid BST
        n = left.n + right.n + 1
    else:
        n = float('-inf')

    largest = max(left.largest, right.largest, n)
    return SubTree(largest, n, min(left.min, root.val), max(right.max, root.val))

if __name__ == '__main__':
    root= TreeNode(5)
    root.left = TreeNode(2)
    root.right = TreeNode(4)

    root.left.left = TreeNode(1)
    root.left.right = TreeNode(3)

    print largestBSTSubtree(root)