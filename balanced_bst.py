#!/usr/bin/env python
'''
Given a binary tree, determine if it is height-balanced.
A height-balanced binary tree is defined as a binary tree in which
the depth of the two subtrees of every node never differ by more than 1.
'''

from binary_tree import BinaryTree

def buildBinaryTree(balanced=True):
    btree = BinaryTree(4)
    btree.insertLeft(3)
    btree.insertRight(10)

    left = btree.getLeft()    # 3
    right = btree.getRight()  # 10

    left.insertLeft(2)      # 4 - 3 - 2
    left.insertRight(4)     # 4 - 3 - 4

    right.insertRight(15)   # 4 - 10 - 15

    left_left = left.getLeft() # 2
    left_left.insertLeft(1)  # 4 - 3 -2 - 1
   

    if not balanced:
        right_right = right.getRight() # 15
        right_right.insertLeft(11)    # 4 - 10 - 15 - 11


    return btree


def check_height(root):
    # height of 0
    if not root:
        return 0

    left_height = check_height(root.getLeft())
    if left_height == -1:
        return -1    # not balanced

    right_height = check_height(root.getRight())
    if right_height == -1:
        return -1    # not balanced

    height = abs(left_height - right_height)
   
    if height > 1:
        return -1    # not balanced
    else:
        return max(left_height, right_height) + 1


def isbalanced(root):
    if check_height(root) == -1:
        return False
    else:
        return True

if __name__ == '__main__':
    tree = buildBinaryTree()
    assert isbalanced(tree)
    print 'Tree is balanced'
    
    tree = buildBinaryTree(balanced=False)
    assert not isbalanced(tree) 
    print 'Tree is NOT balanced'



