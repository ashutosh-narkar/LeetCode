#!/usr/bin/env python
'''
Given a Binary Search Tree (BST), convert it to a Greater Tree such that every key of the original BST is changed
to the original key plus sum of all keys greater than the original key in BST.

Example:

Input: The root of a Binary Search Tree like this:
              5
            /   \
           2     13

Output: The root of a Greater Tree like this:
             18
            /   \
          20     13


Solution:
By leveraging the fact that the tree is a BST, we can find an O(n) solution.
The idea is to traverse BST in reverse inorder.
Reverse inorder traversal of a BST gives us keys in decreasing order.
Before visiting a node, we visit all greater nodes of that node.
While traversing we keep track of sum of keys which is the sum of all the keys greater than the key of current node.


##### Code flow is similar to diameterOfBinaryTree.py ######

'''


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def convert_bst(root):
    """
    :type root: TreeNode
    :rtype: TreeNode
    """

    if not root:
        return None

    # Initialize sum
    result = [0]

    generate_greater_tree(root, result)
    return root


def generate_greater_tree(node, result):
    # Base Case
    if not node:
        return None

    # Recur for right subtree
    generate_greater_tree(node.right, result)

    # Update Sum
    node.val += result[0]
    result[0] = node.val

    # Recur for left subtree
    generate_greater_tree(node.left, result)
