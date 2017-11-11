#!/usr/bin/env python
"""
Given a binary tree, print boundary nodes of the binary tree Anti-Clockwise starting from the root.

For example, boundary traversal of the following tree is "20 8 4 10 14 25 22"

             20
        /         \
        8          22
      /   \          \
    4      12        25
          /  \
        10    14


Solution:

We break the problem in 3 parts:
1. Print the left boundary in top-down manner.
2. Print all leaf nodes from left to right, which can again be sub-divided into two sub-parts:
   2.1 Print all leaf nodes of left sub-tree from left to right.
   2.2 Print all leaf nodes of right subtree from left to right.
3. Print the right boundary in bottom-up manner.

We need to take care of one thing that nodes are not printed again.
e.g. The left most node is also the leaf node of the tree.
"""

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def boundary_of_binary_tree(root):
    if not root:
        return []

    result = list()

    # add the root's value
    result.append(root.val)

    # left boundary
    left_boundary(root.left, result)

    # leaf nodes of left sub-tree
    leaves(root.left, result)

    # leaf nodes of right sub-tree
    leaves(root.right, result)

    # right boundary
    right_boundary(root.right, result)

    return result


# A function to print all left boundary nodes, except a
# leaf node. Print the nodes in TOP DOWN manner
def left_boundary(root, result):
    if not root:
        return

    # leaf node
    if not root.left and not root.right:
        return

    result.append(root.val)

    # keep going left if left child present
    if root.left:
        left_boundary(root.left, result)
    else:
        left_boundary(root.right, result)


# A function to print all right boundary nodes, except
# a leaf node. Print the nodes in BOTTOM UP manner
def right_boundary(root, result):
    if not root:
        return

    # leaf node
    if not root.left and not root.right:
        return

    # keep going right if right child present
    if root.right:
        right_boundary(root.right, result)
    else:
        right_boundary(root.left, result)

    result.append(root.val)      # add after child visit(reverse)


# print leaf nodes using pre-order traversal
def leaves(root, result):
    if not root:
        return

    # leaf node
    if not root.left and not root.right:
        result.append(root.val)
        return

    leaves(root.left, result)
    leaves(root.right, result)

if __name__ == '__main__':

    root = TreeNode(20)
    root.left = TreeNode(8)
    root.right = TreeNode(22)

    root.right.right = TreeNode(25)

    root.left.left = TreeNode(4)

    root.left.right = TreeNode(12)
    root.left.right.left = TreeNode(10)
    root.left.right.right = TreeNode(14)

    print boundary_of_binary_tree(root)
