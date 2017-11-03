#!/usr/bin/env python
'''
Given a singly linked list L: L0 > L1 > … > Ln-1 > Ln,
reorder it to: L0 > Ln > L1 > Ln-1 > L2 > Ln-2 > ...

You must do this in-place without altering the nodes' values.

For example,
Given {1,2,3,4}, reorder it to {1,4,2,3}.

The basic idea is to split the list in half, then reverse the second half, and at last merge them. It is O(n) time, O(1) space.

'''

def reorderList(head):

    if not head:
        return

    # one element in list
    if not head.next:
        return


    # split the list in half
    slow, fast = head, head.next
    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next


    head2 = slow.next
    slow.next  = None


    # reverse second list
    last = None
    current = head2

    while current:
        next = current.next
        current.next = last
        last = current
        current = next

    head2 = last

    # merge first half and reversed second half
    while head2:
        next = head.next
        head.next = head2
        head = head.next
        head2 = next

    return



