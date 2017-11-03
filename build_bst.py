#!/usr/bin/env python
"""
Given an array where elements are sorted in ascending order, convert it to a height balanced BST.

Time Complexity: O(n)
"""

# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def sorted_array_to_bst(num):

    # base case
    if not num:
        return

    # root will be the middle element
    # mid = len(num) / 2
    # below avoids overflow

    low = 0
    high = len(num) - 1
    mid = low + (high - low) / 2

    root = TreeNode(num[mid])

    # everything to left of middle element is part of left subtree
    root.left = sorted_array_to_bst(num[:mid])

    # everything to right of middle element is part of right subtree
    root.right = sorted_array_to_bst(num[mid + 1:])

    return root
