#!/usr/bin/env python
'''
Given a binary tree, flatten it to a linked list in-place.

Eg.

      1
     / \
    2   5
   / \   \
  3   4   6

1
 \
  2
   \
    3
     \
      4
       \
        5  
         \
          6

Solution:

Cut the left child and set to right, the right child is then linked to somewhere behind the left child.
Where should it be then?  Actually the right child should be linked to the most-right node of the left node
'''

def flatten(root):
    while root:
        # if no left child descend to right right child
        if not root.left:
            root = root.right

        else:
            tmp = root.left

            # find the rightmost node of the left child
            # and then attach the right tree to it
            while tmp.right:
                tmp = tmp.right

            tmp.right = root.right
            
            # attach left tree to right tree
            root.right = root.left
       
            # make left tree null
            root.left = None
