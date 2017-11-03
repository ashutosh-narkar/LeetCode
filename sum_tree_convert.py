#!/usr/bin/env python
"""
Given a Binary Tree where each node has positive and negative values.
Convert this to a tree where each node contains the sum of the left and right sub trees in the original tree.
The values of leaf nodes are changed to 0.

For example, the following tree
                  10
               /      \
	         -2        6
           /   \      /  \
	     8     -4    7    5

should be changed to

              20(4-2+12+6)
               /      \
     	   4(8-4)      12(7+5)
           /   \      /  \
	     0      0    0    0


Solution:
Do a traversal of the given tree. In the traversal, store the old value of the current node,
recursively call for left and right subtrees and change the value of current node as sum of the values
returned by the recursive calls.
Finally return the sum of new value and value (which is sum of values in the subtree rooted with this node).

Time Complexity: The solution involves a simple traversal of the given tree.
So the time complexity is O(n) where n is the number of nodes in the given Binary Tree.
"""


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def to_sum_tree(root):
    if not root:
        return 0

    # store the old value
    old_val = root.val

    # Recursively call for left and right subtrees and store the sum as
    # new value of this node
    root.val = to_sum_tree(root.left) + to_sum_tree(root.right)

    # Return the sum of values of nodes in left and right subtrees and
    # old_value of this node
    return root.val + old_val


def inorder(root):
    if not root:
        return

    inorder(root.left)
    print root.val
    inorder(root.right)

if __name__ == '__main__':
    root = TreeNode(10)
    root.left = TreeNode(-2)
    root.right = TreeNode(6)

    root.left.left = TreeNode(8)
    root.left.right = TreeNode(-4)

    root.right.left = TreeNode(7)
    root.right.right = TreeNode(5)

    to_sum_tree(root)

    # Print inorder traversal of the converted tree to test result of toSumTree()
    inorder(root)
