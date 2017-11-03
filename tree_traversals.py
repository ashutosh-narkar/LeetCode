#!/usr/bin/env python
'''
Implement preorder, postorder and inorder tree traversals
http://interactivepython.org/runestone/static/pythonds/Trees/TreeTraversals.html
'''
from binary_tree import BinaryTree
from collections import deque


def buildBinaryTree():
    btree = BinaryTree('0')
    btree.insertLeft('1')
    btree.insertRight('2')
    left = btree.getLeft()
    right = btree.getRight()
    
    left.insertLeft('1.1')
    left.insertRight('1.2')

    right.insertLeft('2.1')
    right.insertRight('2.2')

    left_right = left.getRight()
    left_right.insertLeft('1.2.1')
    left_right.insertRight('1.2.2')

    right_left = right.getRight()
    right_left.insertLeft('2.2.1')
    right_left.insertRight('2.2.2')


    return btree


def preorder(tree):
    if tree:
        print tree.getData()
        preorder(tree.getLeft())
        preorder(tree.getRight())


def postorder(tree):
    if tree:
        postorder(tree.getLeft())
        postorder(tree.getRight())
        print tree.getData()

def inorder(tree):
    if tree:
        inorder(tree.getLeft())
        print tree.getData()
        inorder(tree.getRight())

def level_order(tree):
    '''
    Use BFS to print tree level-by-level
    '''
    if not tree:
        return []
  
    queue = deque()
    queue.append(tree)

    nodesInCurrentLevel = 1
    nodesInNextLevel = 0

    result = []
    temp = []  
 
    while queue:
        node = queue.popleft()
        nodesInCurrentLevel -= 1

        temp.append(node.val)


        if node.getLeft(): 
            queue.append(node.getLeft())
            nodesInNextLevel += 1
   
        
        if node.getRight(): 
            queue.append(node.getRight())
            nodesInNextLevel += 1


        # level ended
        if nodesInCurrentLevel == 0:
            result.append(temp)
            temp = []  

            nodesInCurrentLevel = nodesInNextLevel
            nodesInNextLevel = 0    

    
    return result




if __name__ == '__main__':
    tree = buildBinaryTree()
    print 'Preorder Traversal'
    preorder(tree)

    print 'Postorder Traversal'
    postorder(tree)
     
    print 'Inorder Traversal'
    inorder(tree)

    print 'Level Order Traversal'
    level_order(tree)
