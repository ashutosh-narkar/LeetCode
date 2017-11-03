#!/usr/bin/env python
'''
Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.

If the number of nodes is not a multiple of k then left-out nodes in the end should remain as it is.
You may not alter the values in the nodes, only nodes itself may be changed.

Only constant memory is allowed.

For example,
Given this linked list: 1->2->3->4->5

For k = 2, you should return: 2->1->4->3->5

For k = 3, you should return: 3->2->1->4->5
'''

class ListNode:
    def __init__(self, val):
        self.val = val
        self.next =  None



def reverseKGroup(head, k):

    # create a dummy node and insert at beginning of list
    p = ListNode(0)
    p.next = head
    head = p
    q = head

    while True:
        i = 0
        # advance 'q' by 'k' steps
        while i < k and q:
            q = q.next
            i += 1
   
        # happens if nodes not a multiple of k
        if not q:
            return head.next

        # reverse p.next to q
        while p.next != q:
            tmp1 = p.next
            tmp2 = q.next
            p.next = p.next.next
            q.next = tmp1
            q.next.next = tmp2

        # move 'p' forward by 'k' steps
        for i in range(k):
            p = p.next

        # let 'p' and 'q' point at same node
        q = p


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

    k = 2
    reversed_list = reverseKGroup(node1, k)

    print 'Original list 1 -> 2 -> 3 -> 4 -> 5'

    result = ''
    while reversed_list:
        result += str(reversed_list.val) + ' -> '
        reversed_list = reversed_list.next

    print 'Reversed list by group {} is {}'.format(k, result)
     







            
