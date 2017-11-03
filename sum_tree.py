#!/usr/bin/env python
"""
Check if a given Binary Tree is SumTree

Write a function that returns true if the given Binary Tree is SumTree else false.
A SumTree is a Binary Tree where the value of a node is equal to sum of the nodes present in its left subtree
and right subtree.
An empty tree is SumTree and sum of an empty tree can be considered as 0. A leaf node is also considered as SumTree.

Following is an example of SumTree.

          26
        /   \
      10     3
    /    \     \
  4      6      3

Solution: Get the sum of nodes in left subtree and right subtree.
Check if the sum calculated is equal to root's data.
Also, recursively check if the left and right subtrees are SumTrees.

Time Complexity: O(n^2) in worst case. Worst case occurs for a skewed tree.

For O(n) solution check
"""


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


# Check whether given binary tree satisfies Sum tree
# property or not.
def is_sum_tree(root):

    # empty tree
    if not root:
        return True

    # leaf node
    if not root.left and not root.right:
        return True

    # Find sum of left and right subtree
    left_sum = get_tree_nodes_sum(root.left)
    right_sum = get_tree_nodes_sum(root.right)

    # Check if root node satisfies Sum tree property and
    # also check if both subtree are also sum tree
    if root.val == left_sum + right_sum and is_sum_tree(root.left) and is_sum_tree(root.right):
        return True

    return False


# Return sum of all nodes of a binary tree
def get_tree_nodes_sum(root):
    if not root:
        return 0

    # Recursively calculate the sum of all nodes of
    # left and right sub tree and root node
    return get_tree_nodes_sum(root.left) + root.val + get_tree_nodes_sum(root.right)

if __name__ == '__main__':
    root = TreeNode(26)
    root.left = TreeNode(10)
    root.right = TreeNode(3)

    root.left.left = TreeNode(4)
    root.left.right = TreeNode(6)

    root.right.right = TreeNode(3)

    result = is_sum_tree(root)
    if result:
        print 'Tree is sum tree'
    else:
        print 'Tree is not sum tree'

    # Modifying value of one node to break sun tree property
    root.val = 100
    result = is_sum_tree(root)
    if result:
        print 'Tree is sum tree'
    else:
        print 'Tree is not sum tree'
