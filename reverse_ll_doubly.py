#!/usr/bin/env python
'''
Reverse a doubly linked list
'''

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
        self.prev = None



def reverseList(head):
    if not head:
        return

    current = head
    last = None

    while current:
        next = current.next
        current.prev = next   # ONLY statement to be added compared to singly ll reversal

        current.next = last

        last = current
        current = next
   
    return last

def print_ll(head):
    if not head: 
        return

    current = head

    print 'Printing from head to tail'
    while current:
        print current.val
        current = current.next

    current = head
    while current.next:
        current = current.next

    print '\nPrinting from tail to head'
    while current:
        print current.val
        current = current.prev
 


if __name__ == '__main__':
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(4)

    node1.next = node2

    node2.prev = node1
    node2.next = node3

    node3.prev = node2
    node3.next = node4

    node4.prev = node3

    print 'Original'
    print_ll(node1)

    print '\nReversed'
    rev = reverseList(node1)
    print_ll(rev)
