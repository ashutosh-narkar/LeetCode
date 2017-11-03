#!/usr/bin/env python
'''
Given two binary trees, write a function to check if they are equal or not.

Two binary trees are considered equal if they are structurally identical and the nodes have the same value.
'''
def isSameTree(p, q):

    # both empty
    if not p and not q:
        return True

    # one of them empty	 
    if not p or not q:
        return False

    # val not equal
    if p.val != q.val:
        return False

    return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)
