#!/usr/bin/env python
'''
Given a non-empty special binary tree consisting of nodes with the non-negative value, where each node in this tree
has exactly two or zero sub-node. If the node has two sub-nodes, then this node's value is the smaller
value among its two sub-nodes.

Given such a binary tree, you need to output the second minimum value in the set made of all the nodes' value in the whole tree.

If no such second minimum value exists, output -1 instead.

Example 1:
Input:
    2
   / \
  2   5
     / \
    5   7

Output: 5
Explanation: The smallest value is 2, the second smallest value is 5.

Example 2:
Input:
    2
   / \
  2   2

Output: -1
Explanation: The smallest value is 2, but there isn't any second smallest value.
'''


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# Solution 1:
# Based on the problem description, the root node will always have the minimum value of the whole tree.
# This property also holds true for any subtree.
# Now we can turn the problem to "find the minimum value in the tree that is greater
# than the root's value -- call it min1".

# if node.val > min1, we know all values in the subtree at node are at least node.val,
# so there cannot be a better candidate for the second minimum in this subtree.
# Thus, we do not need to search this subtree.

def findSecondMinimumValue(root):
    """
    :type root: TreeNode
    :rtype: int
    """
    if not root:
        return -1

    result = [0]
    result[0] = float('inf')
    min1 = root.val

    helper(root, result, min1)

    if result[0] < float('inf'):
        return result[0]

    return -1


def helper(node, result, min1):
    if node:
        if min1 < node.val < result[0]:
            result[0] = node.val
        elif min1 == node.val:
            helper(node.left, result, min1)
            helper(node.right, result, min1)


# Solution 2:
class Solution(object):
    def findSecondMinimumValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return -1

        if not root.left and not root.right:
            return -1

        left_res, right_res = root.left.val, root.right.val

        if root.val == left_res:
            left_res = self.findSecondMinimumValue(root.left)

        if root.val == right_res:
            right_res = self.findSecondMinimumValue(root.right)

        if left_res == -1 and right_res > -1:
            return right_res

        if left_res > -1 and right_res == -1:
            return left_res

        return min(left_res, right_res)