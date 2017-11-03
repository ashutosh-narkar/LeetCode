#!/usr/bin/env python
'''
Print all paths in a binary tree

Runtime = O(n)
'''
from binary_tree import BinaryTree


def buildBinaryTree():
    btree = BinaryTree('0')
    btree.insertLeft('1')
    btree.insertRight('5')
    left = btree.getLeft()
    right = btree.getRight()

    left.insertLeft('2')
    left.insertRight('3')

    right.insertLeft('6')

    left_right = left.getRight()
    left_right.insertLeft('4')


    return btree


def print_all_paths(root, val='', result=[]):
    '''
    Given the tree, calculate sum of all paths
    '''
    # base case
    if not root:
        return
   
    # update val
    val += root.getData()

    # if current node is leaf, store the path
    if not (root.getLeft() or root.getRight()):
        result.append(val)
        return
   
    # recur for left and right subtree 
    left = print_all_paths(root.getLeft(), val, result)
    right = print_all_paths(root.getRight(), val, result)
    return result


if __name__ == '__main__':
    root = buildBinaryTree()
    print print_all_paths(root)        
    

