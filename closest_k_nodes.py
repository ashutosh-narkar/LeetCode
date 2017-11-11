#!/usr/bin/env python
"""
Given a binary tree, a target node in the binary tree, and an integer value k,
find k nodes that are closest to the target node. No parent pointers are available.
"""


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def closestKValues(root, target, k):
    result = []
    inorder(root, target, k, result)
    return result


def inorder(root, target, k, result):
    if not root:
        return

    inorder(root.left, target, k, result)

    if len(result) < k:
        result.append(root.val)

    elif abs(root.val - target) < abs(result[0] - target):
        result.pop(0)
        result.append(root.val)

    else:
        return

    inorder(root.right, target, k, result)

if __name__ == "__main__":
    root = TreeNode(20)
    root.left = TreeNode(8)
    root.right = TreeNode(22)

    root.left.left = TreeNode(4)
    root.left.right = TreeNode(12)

    root.left.right.left = TreeNode(10)
    root.left.right.right = TreeNode(14)

    print closestKValues(root, 14, 1)
