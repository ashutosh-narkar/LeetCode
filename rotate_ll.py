#!/usr/bin/env python
'''
Given a list, rotate the list  by k places, where k is non-negative.

'''
import sys

# Definition for singly-linked list.

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def rotateLeft(head, k):

    if k == 0:
        return head

    if not head:
        return

    current = head

    i  = 1
    while i < k:
        if not current:
            return
        current = current.next
        i += 1

    if not current:
        return

    kthNode = current

    # after this current points to last node
    while current.next:
        current = current.next

    current.next = head
    head = kthNode.next
    kthNode.next = None

    return head



def rotateRight(head, k):

    if not head:
        return

    size = 0
    current = head

    while current:
        size += 1
        current = current.next

    k  = k % size

    if k == 0:
        return head


    k  = size - k

    current = head
    i  = 1
    while i < k:
        if not current:
            return
        current = current.next
        i += 1

    if not current:
        return

    kthNode = current

    # after this current points to last node
    while current.next:
        current = current.next

    current.next = head
    head =  kthNode.next
    kthNode.next = None

    return head



if __name__ == '__main__':
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(4)
    node5 = ListNode(5)

    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5

    print 'Original list: 1 -> 2 -> 3 -> 4 -> 5'
    k = int(sys.argv[1])

    res = rotateRight(node1, k)
    result = ''

    while res:
        result += str(res.val) + ' -> '
        res = res.next

    print 'Right Rotated by {}: {}'.format(k, result)
    













