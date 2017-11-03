#!/usr/bin/env python
'''
Given a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.

You should preserve the original relative order of the nodes in each of the two partitions.

For example,
Given 1->4->3->2->5->2 and x = 3,
return 1->2->2->4->3->5.


Solution:

the basic idea is to maintain two lists, the first one stores all nodes with val less than x , 
and the second queue stores all the rest nodes. 
Then concat these two queues. Remember to set the tail of second queue a null next, or u will get TLE.
'''

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def partition(head, x):

    if not head:
        return

    # dummy  lists
    p = ListNode(0)
    q = ListNode(0)

    current = head
    current1, current2 = p, q

    while current:
        # move first list ahead
        if current.val < x:
            current1.next = current
            current1 = current1.next

        # move 2nd list ahead
        else:
            current2.next = current
            current2 = current2.next

        current = current.next

    # link the lists.
    current1.next = q.next

    # avoid cycle in linked list
    current2.next = None

    return p.next
