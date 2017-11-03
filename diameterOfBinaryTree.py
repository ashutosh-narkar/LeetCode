#!/usr/bin/env python
'''
Given a binary tree, you need to compute the length of the diameter of the tree.
The diameter of a binary tree is the length of the longest path between any two nodes in a tree.
This path may or may not pass through the root.

Given a binary tree
          1
         / \
        2   3
       / \
      4   5
Return 3, which is the length of the path [4,2,1,3] or [5,2,1,3].

Solution:
The diameter of a tree T is the largest of the following quantities:

* the diameter of T's left subtree
* the diameter of T's right subtree
* the longest path between leaves that goes through the root of T (this can be computed from the heights of the subtrees of T)
'''


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

def diameterOfBinaryTree(root):
    """
    :type root: TreeNode
    :rtype: int
    """
    if not root:
        return 0

    ans = [0]
    depth(root, ans)
    return ans[0]


def depth(node, result):
    if not node:
        return 0

    left = depth(node.left, result)
    right = depth(node.right, result)

    result[0] = max(result[0], left + right)

    return max(left, right) + 1