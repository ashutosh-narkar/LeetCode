#!/usr/bin/env python
"""
Given a Binary Tree find the length of the longest path which comprises of nodes with consecutive values
in increasing order. Every node is considered as a path of length 1.

Example 1:

    6
      \
       9
     /   \
    7     10
           \
            11

Longest consecutive path = 9, 10, 11. Length = 3


Example 2:
        1
      /  \
     2    4
    /    / \
   3    5   6
           /
          7

Longest consecutive path = 1, 2, 3. Length = 3

Solution: Pre-Order Traversal. Just send cur node value to the next level and compare it with the next level node.

"""


class TreeNode:
    def __init__(self, val):
        self.val =val
        self.left = None
        self.right = None


def longest_consecutive(root):
    if not root:
        return 0

    result = [0]
    helper(root, result, root.val, 0)
    return result[0]


def helper(root, result, target, curr_length):
    if not root:
        return

    if root.val == target:
        curr_length += 1                # streak continues
    else:
        curr_length = 1                 # start new streak

    # update result
    result[0] = max(result[0], curr_length)

    helper(root.left, result, root.val + 1, curr_length)           # find next consecutive number in left sub-tree
    helper(root.right, result, root.val + 1, curr_length)          # find next consecutive number in right sub-tree


if __name__ == '__main__':

    # Example 1
    root = TreeNode(6)
    root.right = TreeNode(9)

    root.right.left = TreeNode(7)
    root.right.right = TreeNode(10)

    root.right.right.right = TreeNode(11)

    print longest_consecutive(root)

    # Example 2
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.left.left = TreeNode(3)

    root.right = TreeNode(4)
    root.right.left = TreeNode(5)
    root.right.right = TreeNode(6)

    root.right.right.left = TreeNode(7)

    print longest_consecutive(root)
