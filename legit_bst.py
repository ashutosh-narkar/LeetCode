#!/usr/bin/env python
'''
Check if a BST is legit OR Given binary tree is a Binary Search Tree (BST) or not.

Do a inorder traversal of the tree and check if previous value is <= current value. Runtime O(n)
'''
from binary_tree import BinaryTree


def buildLegitBinaryTree():
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


    right_right = right.getRight() # 15
    right_right.insertLeft(11)    # 4 - 10 - 15 - 11


    return btree

def buildNotLegitBinaryTree():

     # Example -1
#    btree = BinaryTree(4)
#    btree.insertLeft(3)
#    btree.insertRight(10)
#
#    left = btree.getLeft()    # 3
#    right = btree.getRight()  # 10
#
#    left.insertLeft(2)      # 4 - 3 - 2
#    left.insertRight(4)     # 4 - 3 - 4
#
#    right.insertRight(5)   # 4 - 10 - 5
#
#    right.insertLeft(9)    # 4 - 10 - 9
#

    # Example -2
    btree = BinaryTree(10)
    btree.insertLeft(5)
    btree.insertRight(15)
    
    right = btree.getRight()  # 15
    right.insertLeft(6)    # 10 - 15 - 6
    right.insertRight(20)   # 10 - 15 - 20

    return btree
    


def isValidBST(root):
    """
    :type root: TreeNode
    :rtype: bool
    """
    if not root:
        return True

    result = []
    inOrder(root, result)

    for i in range(len(result) - 1):
        if result[i] < result[i + 1]:
            continue
        return False

    return True


def inOrder(tree, result):
    if not tree:
        return

    inOrder(tree.left, result)
    result.append(tree.val)
    inOrder(tree.right, result)




   
if __name__ == '__main__':
    tree = buildLegitBinaryTree()
    res = islegit(tree)    

    if res:
        print 'Valid BST'
    else:
        print 'Not Valid BST'

    tree = buildNotLegitBinaryTree()
    res = islegit(tree)

    if res:
        print 'Valid BST'
    else:
        print 'Not Valid BST'

