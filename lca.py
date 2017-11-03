#!/usr/bin/env python
'''
Given a binary tree, find the lowest(deepest) common ancestor of two given nodes in the tree.
Runtime O(n)
'''

def lca(root, node1, node2):

    # base case
    if not root:
        return

    if root == node1 or root == node2:
        return root

    left = lca(root.left, node1, node2)
    right = lca(root.right, node1, node2)

    # nodes in opposite subtrees
    if left and right:
        return root

    # both nodes in left subtree
    if left:
        return left

    # both nodes in right subtree
    return right




'''
Given a binary tree, find the lowest common ancestor of two given nodes in the tree.
Each node contains a parent pointer which links to its parent.
'''

def lca_2(node1, node2):
    visited = set()
 
    while p or q:
        if p and q in visited:
            return p
        else:
            visited.add(p)
            p = p.parent

        if q and p in visited:
            return q
        else:
            visited.add(q)
            q = q.parent

    return
