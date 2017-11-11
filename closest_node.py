#!/usr/bin/env python
"""
Given a non-empty binary search tree and a target value, find the value in the BST that is closest to the target.

**** THIS IS A SPECIAL CASE OF closest_k_nodes.py WITH K = 1 ****
"""

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def closestValue(root, target):
    if not root:
        return

    result = [0] * 2
    result[0] = float('inf')     # min diff
    result[1] = 0                # closest value

    helper(root, target, result)
    return result[1]


def helper(root, target, result):
    if not root:
        return

    if abs(root.val - target) < result[0]:
        result[0] = abs(root.val - target)
        result[1] = root.val

    if root.val < target:
        helper(root.right, target, result)
    else:
        helper(root.left, target, result)


if __name__ == '__main__':
    root = TreeNode(20)
    root.left = TreeNode(8)
    root.right = TreeNode(22)

    root.left.left = TreeNode(4)
    root.left.right = TreeNode(12)

    root.left.right.left = TreeNode(10)
    root.left.right.right = TreeNode(14)

    print closestValue(root, 16)