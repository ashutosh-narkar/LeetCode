#!/usr/bin/env python
"""
Given a Binary Search Tree (BST) and a range, count number of nodes that lie in the given range.

Examples:

Input:
        10
      /    \
    5       50
   /       /  \
 1       40   100
Range: [5, 45]

Output:  3
There are three nodes in range, 5, 10 and 40

Solution: In-order traversal
"""

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def get_count(root, low, high):
    if not root:
        return 0

    # If current node is in range, then include it in count and
    # recur for left and right children of it
    if low <= root.val <= high:
        return 1 + get_count(root.left, low, high) + get_count(root.right, low, high)

    # If current node is smaller than low, then recur for right child
    elif root.val < low:
        return get_count(root.right, low, high)

    # Else recur for left child
    else:
        return get_count(root.left, low, high)

if __name__ == '__main__':
    root = TreeNode(10)
    root.left = TreeNode(5)
    root.right = TreeNode(50)

    root.left.left = TreeNode(1)
    root.right.left = TreeNode(40)
    root.right.right = TreeNode(100)

    print get_count(root, 5, 45)
