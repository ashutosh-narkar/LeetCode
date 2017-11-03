#!/usr/bin/env python
"""
Two elements of a binary search tree (BST) are swapped by mistake.
Recover the tree without changing its structure.

Constant Space solution needed

Solution:

We need to find the first and second elements that are not in order right?

How do we find these two elements? For example, we have the following tree that is printed as in order traversal:

6, 3, 4, 5, 2

We compare each node with its next one and we can find out that 6 is the first element to swap because 6 > 3 and 2 is the second element to swap because 2 < 5.

Really, what we are comparing is the current node and its previous node in the "in order traversal".
"""


# Definition for a binary tree node.
class TreeNode(object):
     def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):

    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        if not root:
            return

        # The reason for this initialization is to avoid null pointer exception
        # in the first comparison when 'prev' has not been initialized
        self.prev = TreeNode(float('-inf'))
        self.first = None
        self.second = None

        # In order traversal to find the two elements
        self.in_order(root)

        # Swap the values of the two nodes
        self.first.val, self.second.val = self.second.val, self.first.val

    def in_order(self, root):
        if not root:
            return

        # Go left
        self.in_order(root.left)

        # Implement business logic

        # If first element has not been found, assign it to prevElement (refer to 6 in the example above)
        if not self.first and self.prev.val >= root.val:
            self.first = self.prev

        #  If first element is found, assign the second element to the root (refer to 2 in the example above)
        if self.first and self.prev.val >= root.val:
            self.second = root

        self.prev = root


        # Go right
        self.in_order(root.right)