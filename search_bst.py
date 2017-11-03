#!/usr/bin/env python
'''
Write a function that takes a BST T and a key k, and returns the
first entry larger than k that would appear in an inorder traversal. If k is absent or no key
larger than k is present, return null.

Solution:
1) If the current node’s key is larger than k, we update first to the current node and continue
the search in the left subtree. 

2) If the current node’s key is smaller than k, we search
in the right subtree. 

3) If the current node’s key is equal to k, we set a Boolean-valued
found_k variable to true, and continue search in the current node’s right subtree.


4) When the current node becomes null, if found_k is true we return first, otherwise
we return null. 

Correctness follows from the fact that after first is assigned within
the loop, the desired result is within the tree rooted at first.

The time complexity is O(h), where h is the height of the tree. The space complexity
is O(1).

****** Refer solution successor_binary_tree.py ****************


'''
def find_first_larger_k(root, k):

    if not root:
        return

    first = None

    found_k = False

    while root:
        if root.data == k:
            found_k = True
            root = root.right


        elif root.data < k:
            root = root.right

        else:
            first = root
            root = root.left


    if not found_k:
        return

    return first
        
