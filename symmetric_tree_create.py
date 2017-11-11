#!/usr/bin/env python
"""
Convert a Binary Tree into its Mirror Tree

Example:

    1
3       2
      5   4

Mirror of above tree

      1
  2      3
4   5

Solution: Post-order traversal
"""

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def mirror_tree(root):
    if not root:
        return

    left = mirror_tree(root.left)
    right = mirror_tree(root.right)

    # swap the left and right pointers
    root.left = right
    root.right = left

    return root


def inorder(root):
    if not root:
        return

    inorder(root.left)
    print root.val
    inorder(root.right)


if __name__ == '__main__':
    root = Node(1)
    root.left = Node(3)
    root.right = Node(2)

    root.right.left = Node(5)
    root.right.right = Node(4)

    print 'Original Tree'
    inorder(root)

    print '\nMirror Tree'
    mirror = mirror_tree(root)
    inorder(mirror)
