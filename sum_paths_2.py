#!/usr/bin/env python
'''
Given a binary tree and a sum, determine if the tree has a root-to-leaf path 
such that adding up all the values along the path equals the given sum.

For example:
Given the below binary tree and sum = 22,
              5
             / \
            4   8
           /   / \
          11  13  4
         /  \      \
        7    2      1
return true, as there exist a root-to-leaf path 5->4->11->2 which sum is 22.

********* Alternate Question**********
Find the maximum sum leaf to root path in a Binary Tree 

Runtime = O(n)
'''

def hasPathSum(root, sum):

    if not root:
        return False

    result  = []
    traverse(root, result)

    return sum in result

        

def traverse(root, result, val=0):
    if not root:
        return

    val = val + root.val

    if not (root.left or root.right):
        result.append(val)


    traverse(root.left, result, val)
    traverse(root.right, result, val)
 

