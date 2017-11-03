#!/usr/bin/env python
'''
Given two binary trees and imagine that when you put one of them to cover the other, some nodes of the two trees are overlapped while the others are not.

You need to merge them into a new binary tree. The merge rule is that if two nodes overlap, then sum node values up as the new value of the merged node.
Otherwise, the NOT null node will be used as the node of new tree.

Input:
	Tree 1                     Tree 2

          1                         2
         / \                       / \
        3   2                     1   3
       /                           \   \
      5                             4   7
Output:
Merged tree:
	     3
	    / \
	   4   5
	  / \   \
	 5   4   7


Note: The merging process must start from the root nodes of both trees.
'''

# Solution 1: Iterative .
# Time complexity : O(n). We traverse over a total of n nodes. Here, n refers to the smaller of the number of nodes in the two trees.
# Space complexity : O(n). The depth of stack can grow upto n in case of a skewed tree.

def mergeTrees(t1, t2):
    """
    :type t1: TreeNode
    :type t2: TreeNode
    :rtype: TreeNode
    """
    if not t1:
        return t2

    stack = []
    stack.append([t1, t2])

    while stack:
        node1, node2 = stack.pop()

        if not node1 or not node2:
            continue

        # increment the current node's value
        node1.val += node2.val

        # left child
        # if the current node of the 1st tree has no left child, simply use the 2nd tree's left child.
        # Otherwise, push the left children of both trees on stack
        if not node1.left:
            node1.left = node2.left

        else:
            stack.append([node1.left, node2.left])

        # right child
        # if the current node of the 1st tree has no right child, simply use the 2nd tree's right child.
        # Otherwise, push the right children of both trees on stack
        if not node1.right:
            node1.right = node2.right

        else:
            stack.append([node1.right, node2.right])

    return t1



# Solution 2:  Recursive
# Time complexity : O(m). A total of m nodes need to be traversed. Here, m represents the minimum number of nodes from the two given trees.
#Space complexity : O(m). The depth of the recursion tree can go upto m in the case of a skewed tree. In average case, depth will be O(logm).

def mergeTrees(t1, t2):
    """
    :type t1: TreeNode
    :type t2: TreeNode
    :rtype: TreeNode
    """
    if not t1:
        return t2

    if not t2:
        return t1

    t1.val += t2.val

    t1.left = mergeTrees(t1.left, t2.left)
    t1.right = mergeTrees(t1.right, t2.right)

    return t1
