#!/usr/bin/env python
'''
Given a linked list, remove the nth node from the end of list and return its head.

For example,

Given linked list: 1->2->3->4->5, and n = 2.
After removing the second node from the end, the linked list becomes 1->2->3->5.

Note:
Given n will always be valid.
'''
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# Solution 1: One pass
# Use fast and slow pointers. The fast pointer is 'n' steps ahead of the slow pointer.
# When the fast reaches the end, the slow pointer points at the previous element of the target element.

def removeNthFromEnd(head, n):
    """
    :type head: ListNode
    :type n: int
    :rtype: ListNode
    """
    if not head:
        return

    slow = head
    fast = head

    # Move fast pointer 'n' steps ahead of slow pointer
    for _ in range(n):
        fast = fast.next

    # remove the first node
    if not fast:
        return head.next

    # Move fast pointer to the end, maintaining the gap
    while fast.next:
        fast = fast.next
        slow = slow.next

    # Skip the desired node
    slow.next = slow.next.next

    return head


# Solution 2: Two pass
def removeNthFromEnd_1(head, n):

    if not head:
        return

    size = 0
    current = head

    # get size of ll
    while current:
        size += 1
        current = current.next


    p = ListNode(0)
    p.next = head
    head = p
    current = p


    for i in range(size - n):
        current = current.next

    # current points to node before one to be removed
    current.next = current.next.next

    # since p is a dummy node
    return p.next



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


    print 'Original List 1 -> 2 -> 3 -> 4 -> 5'

    n = 2
    res = removeNthFromEnd_2(node1, n)

    result = ''
    while res:
        result += str(res.val) + ' -> '
        res = res.next

    print result










