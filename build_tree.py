#!/usr/bin/env python
'''
Given preorder(OR postorder) and inorder traversal of a tree, construct the binary tree.
Assume no duplicate elements

Runtime O(n)
'''

from collections import deque

class TreeNode:

    def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None


def buildInorderPreorder(preorder, inorder):
    if not inorder or not preorder:
        return 

    # since we pop(0), we don't need to slice the preorder array, 
    #i when we are done with the left tree, the left half of the preorder array should already be empty

    rootVal = preorder.pop(0)
    rootIndex = inorder.index(rootVal)

    root = TreeNode(rootVal)
    root.left = buildInorderPreorder(preorder, inorder[:rootIndex])
    root.right = buildInorderPreorder(preorder, inorder[rootIndex + 1:])

    return root


def buildInorderPreorder_2(preorder, inorder):
    if not inorder or not preorder:
        return

    # if we do not pop(0)
    rootVal = preorder[0]
    rootIndex = inorder.index(rootVal)

    root = TreeNode(rootVal)
    root.left = buildInorderPreorder_2(preorder[1: rootIndex + 1], inorder[:rootIndex])
    root.right = buildInorderPreorder_2(preorder[rootIndex + 1:], inorder[rootIndex + 1:])

    return root

def buildInorderPostorder(inorder, postorder):


    if not inorder or not postorder:
        return


    rootVal = postorder.pop()
    rootIndex = inorder.index(rootVal)


    root = TreeNode(rootVal)

    # since we pop the last element, we need to build right tree first
    # else we will get a Value error
    # eg. [2,1,3], [2,3,1]    ValueError: 3 is not in list
    root.right = self.buildTree(inorder[rootIndex + 1:], postorder)
    root.left = self.buildTree(inorder[:rootIndex], postorder)


    return root


def buildInorderPostorder_2(inorder, postorder):
    if not inorder or not postorder:
        return 

 
    rootVal = postorder[-1]
    rootIndex = inorder.index(rootVal) 

    root = TreeNode(rootVal)
    root.left = buildInorderPostorder_2(inorder[:rootIndex], postorder[:rootIndex])
    root.right = buildInorderPostorder_2(inorder[rootIndex + 1:], postorder[rootIndex: -1])
  
    return root



def printTreeLevel(root):
    if not root:
        return
 
    queue = deque()
    queue.append(root)

    currentLevelNodes = 1
    nextLevelNodes = 0

    while queue:
        node = queue.popleft()
        currentLevelNodes -= 1
        
        print node.getData()
        
        if node.getLeft():
            queue.append(node.getLeft())
            nextLevelNodes += 1

        if node.getRight():
            queue.append(node.getRight())
            nextLevelNodes += 1

        if currentLevelNodes == 0:
            print '\n' 
            currentLevelNodes, nextLevelNodes = nextLevelNodes, 0


 
