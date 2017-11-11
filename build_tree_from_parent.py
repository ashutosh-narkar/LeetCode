#!/usr/bin/env python
"""
Given an array that represents a tree in such a way that array indexes are values in tree nodes
and array values give the parent node of that particular index (or node).
The value of the root node index would always be -1 as there is no parent for root.

Construct the standard linked representation of given Binary Tree from this given representation.

Input: parent[] = {1, 5, 5, 2, 2, -1, 3}
Output: root of below tree
          5
        /  \
       1    2
      /    / \
     0    3   4
         /
        6
Explanation:
Index of -1 is 5.  So 5 is root.
5 is present at indexes 1 and 2.  So 1 and 2 are
children of 5.
1 is present at index 0, so 0 is child of 1.
2 is present at indexes 3 and 4.  So 3 and 4 are
children of 2.
3 is present at index 6, so 6 is child of 3.


Input: parent[] = {-1, 0, 0, 1, 1, 3, 5};
Output: root of below tree
         0
       /   \
      1     2
     / \
    3   4
   /
  5
 /
6

"""


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

""" 
Creates a node with key as 'i'. If i is root,then
it changes root. If parent of i is not created, then
it creates parent first 
"""


def createNode(parent, i, created, root):

    # If this node is already created
    if created[i]:
        return

    # Create a new node and set created[i]
    created[i] = Node(i)

    # If 'i' is root, change root pointer and return
    if parent[i] == -1:
        root[0] = created[i]  # root[0] denotes root of the tree
        return

    # If parent is not created, then create parent first
    if not created[parent[i]]:
        createNode(parent, parent[i], created, root)

    # Find parent pointer
    p = created[parent[i]]

    # If this is first child of parent
    if p.left is None:
        p.left = created[i]

    # If second child
    else:
        p.right = created[i]


# Creates tree from parent[0..n-1] and returns root of the
# created tree
def createTree(parent):
    n = len(parent)

    # Create and array created[] to keep track
    # of created nodes, initialize all entries as None
    created = [None for i in range(n + 1)]

    root = [None]
    for i in range(n):
        createNode(parent, i, created, root)

    return root[0]


# Inorder traversal of tree
def inorder(root):
    if not root:
        return

    inorder(root.left)
    print root.val
    inorder(root.right)

if __name__ == '__main__':
    parent = [-1, 0, 0, 1, 1, 3, 5]
    root = createTree(parent)
    print "Inorder Traversal of constructed tree"
    inorder(root)
