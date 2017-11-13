#!/usr/bin/env python
"""
Given a binary search tree, write a function kthSmallest to find the kth smallest element in it.

Note:
You may assume k is always valid, 1 <= k <= BST's total elements.
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# Solution 1: Each node tracks the order, i.e., the number of elements that are less than itself
# Runtime: O(logn)
def kthSmallest(root, k):
    """
    :type root: TreeNode
    :type k: int
    :rtype: int
    """
    if not root:
        return 0

    stack = []
    current = root
    rank = 0

    while stack or current:
        if current:
            stack.append(current)
            current = current.left     # like in-order traversal we go left

        else:
            current = stack.pop()
            rank += 1
            if rank == k:
                return current.val
            current = current.right

    return float('-inf')


# Solution 2: Inorder Traversal
# Runtime: O(n)
def kthSmallest(root, k):
    """
    :type root: TreeNode
    :type k: int
    :rtype: int
    """
    if not root:
        return 0

    result = []
    inorder(root, result)

    return result[k - 1]


def inorder(root, result):
    if not root:
        return

    inorder(root.left, result)
    result.append(root.val)
    inorder(root.right, result)