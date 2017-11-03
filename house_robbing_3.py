#!/usr/bin/env python
'''
The thief has found himself a new place for his thievery again. There is only one entrance to this area, called the "root."
Besides the root, each house has one and only one parent house.
After a tour, the smart thief realized that "all houses in this place forms a binary tree".
It will automatically contact the police if two directly-linked houses were broken into on the same night.

Determine the maximum amount of money the thief can rob tonight without alerting the police.

Example 1:
     3
    / \
   2   3
    \   \
     3   1
Maximum amount of money the thief can rob = 3 + 3 + 1 = 7.

Example 2:
     3
    / \
   4   5
  / \   \
 1   3   1
Maximum amount of money the thief can rob = 4 + 5 = 9.

Solution:
dfs all the nodes of the tree, each node returns two numbers, int[] num,
num[0] is the max value if this node is robbed,
num[1] is the max value if this node is NOT robbed.

Current node's return value only depends on its children's value.
'''


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0

        res = dfs(root)
        return max(res)  # max(res[0], res[1])


def dfs(node):
    if not node:
        return [0, 0]

    left = dfs(node.left)
    right = dfs(node.right)

    res = [0] * 2

    # if this node is robbbed, its left and right child cannot be robbed
    res[0] = node.val + left[1] + right[1]

    # if this node is not robbed, left and/or right child CAN be robbed
    res[1] = max(left[0], left[1]) + max(right[0], right[1])

    return res