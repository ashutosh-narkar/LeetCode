#!/usr/bin/env python
"""
Merge Sort in a Linked list
"""


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


def sort(head):

    # if head is empty or only one node in linked list
    if not head or not head.next:
        return head

    # find the middle of linked list
    slow = head
    fast = head.next

    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next

    head2 = slow.next

    # split the linked lists
    slow.next = None

    left = sort(head)
    right = sort(head2)

    return merge(left, right)


# merge two linked lists
def merge(l1, l2):
    # create a dummy node
    dummy = Node(0)
    current = dummy

    while current:
        if not l1:
            current.next = l2
            break

        elif not l2:
            current.next = l1
            break

        elif l1.val < l2.val:
            current.next = l1
            l1 = l1.next

        else:
            current.next = l2
            l2 = l2.next

        current = current.next

    return dummy.next

if __name__ == '__main__':

    # create unsorted linked list
    # 2->3->20->5->10->15
    a = Node(2)
    b = Node(3)
    c = Node(20)
    d = Node(5)
    e = Node(10)
    f = Node(15)
    a.next = b
    b.next = c
    c.next = d
    d.next = e
    e.next = f

    print "Unsorted Linked List"
    current = a
    while current:
        print current.val
        current = current.next

    print '\n'

    current1 = sort(a)
    print "Sorted Linked List"
    while current1:
        print current1.val
        current1 = current1.next
