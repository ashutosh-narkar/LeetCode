#!/usr/bin/env python
'''
Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.

For example:
Given the below binary tree and sum = 22,

              5
             / \
            4   8
           /   / \
          11  13  4
         /  \    / \
        7    2  5   1

return
[
   [5,4,11,2],
   [5,8,4,5]
]
'''

def pathSum(root, sum):
    if not root:
        return []

    result = []

    traverse(root, result, sum)
    return result


def traverse(root, result, sum, temp=[], val=0):

    if not root:
	    return

    val += root.data
    temp.append(root.data)

    if not root.left and not root.right and val == sum:
        result.append(list(temp))

        # don't forget to remove the last integer
        temp.pop()
        return

   
    traverse(root.left, result, sum, temp, val)
    traverse(root.right, result, sum, temp, val)

    # After searching the left node and right node, DO NOT forget to pop the node added in the vector.
    temp.pop()
