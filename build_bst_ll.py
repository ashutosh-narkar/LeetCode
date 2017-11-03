#!/usr/bin/env python
'''
Given a singly linked list where elements are sorted in ascending order, convert it to a height balanced BST.

Runtime - O(nlogn)
a =2, b=2, d=1 ..use Master Method

'''

# Definition for a  binary tree node

class TreeNode:

     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None


#Definition for singly-linked list.

class ListNode:

     def __init__(self, x):
         self.val = x
         self.next = None


def sortedListToBST(head):

    if not head:
        return

    # one node
    if not head.next:
        return TreeNode(head.val)

    # find mid node
    slow, fast = head, head.next

    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next

    mid = slow.next
    root = TreeNode(mid.val)
    
    # this will partition the list
    slow.next = None
    
    root.left = sortedListToBST(head)
    root.right = sortedListToBST(mid.next)

    return root
