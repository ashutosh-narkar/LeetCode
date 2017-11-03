#!/usr/bin/env python
'''
Given a binary tree, imagine yourself standing on the right side of it,
return the values of the nodes you can see ordered from top to bottom.

For example:
Given the following binary tree,
   1            <---
 /   \
2     3         <---
 \     \
  5     4       <---
You should return [1, 3, 4].

'''

from collections import deque


# Definition for a  binary tree node
class TreeNode:

     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None


# @param root, a tree node
# @return a list of integers
def rightSideView(root):

    if not root:
        return []
 
    queue = deque()
    queue.append(root)

    # number of nodes in current and next level
    nodeCurr, nodeNext = 1, 0
    result = []

    while queue:
        node = queue.popleft()
        nodeCurr -= 1

        if node.left:
            queue.append(node.left)
            nodeNext += 1

        if node.right:
            queue.append(node.right)
            nodeNext += 1

        if nodeCurr == 0:
            result.append(node.val)
            nodeCurr, nodeNext = nodeNext, 0 
            
    return result


#### To get the leftSideView, add the right child first and then the left child


