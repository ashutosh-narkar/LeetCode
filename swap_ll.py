#!/usr/bin/env python
'''
Given a linked list, swap every two adjacent nodes and return its head.

For example,
Given 1->2->3->4, you should return the list as 2->1->4->3.

Your algorithm should use only constant space. You may not modify the values in the list, only nodes itself can be changed.
'''
def swapPairs(self, head):

    if not head:
	    return

    p = head
    q = head

    while True:

	    q = p.next
	    if not q:
	        return head

	    #swap
	    p.val, q.val = q.val, p.val
	
	    if not q.next:
	        return head
	    p = q.next
        

