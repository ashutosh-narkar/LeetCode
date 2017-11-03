#!/usr/bin/env python
'''
Given a binary tree where all the right nodes are either leaf nodes with a sibling (a left node that shares the same parent node) or empty, 
flip it upside down and turn it into a tree where the original right nodes turned into left leaf nodes. Return the new root.

For example:
Given a binary tree {1,2,3,4,5},
      1
    /   \
   2     3
  / \
 4   5

return the root of the binary tree [4,5,2,#,#,3,1].
       4
     /   \
    5     2
         / \
        3   1
'''
def upsideDownBinaryTree(root):

    stack = []

    # dummy node
    head = TreeNode(0)
    current = head

    # traversal until the very left node, use a stack to store each node traveled.
    while(root):
        stack.append(root.val)
        root = root.left

    
    while stack:
        node = stack.pop()
        current.right = node
        
        if stack:
            node.left = stack[-1].right

        current = current.right

    return head.right   


# Constant space and O(n)
def upsideDownBinaryTree(root): 
    current = root
    prev, next, temp = [None] * 3 

    while current:
        next = current.left
        current.left = temp
        temp = current.right
        current.right = prev
        prev = current
        current = next

    return prev   




















