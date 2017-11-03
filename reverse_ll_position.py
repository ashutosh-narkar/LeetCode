#!/usr/bin/env python
'''
Reverse a linked list from position m to n. Do it in-place and in one-pass.

For example:
Given 1->2->3->4->5->NULL, m = 2 and n = 4,

return 1->4->3->2->5->NULL.

Note:
Given m, n satisfy the following condition:
1 <= m <= n <= length of list.
'''

class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

def reverseBetween(head, m, n):
    if not head:
        return


    # create a dummy node and make it new head
    p = ListNode(0)
    p.next = head
    head = p
    q = head

    

    while True:
        
        # move p by 'm - 1' steps since, we want to land on node before mth node
	    for i in range(m - 1):
	        p = p.next

        # move q by 'n' steps
	    for i in range(n):
	        q = q.next

	    while p.next != q:
	        tmp1 = p.next
	        tmp2 = q.next
	        p.next = p.next.next
	        q.next = tmp1
	        q.next.next = tmp2

	    return head.next

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

    m = 2
    n = 4
    reversed_list = reverseBetween(node1, m, n)

    print 'Original list 1 -> 2 -> 3 -> 4 -> 5'

    result = ''
    while reversed_list:
        result += str(reversed_list.val) + ' -> '
        reversed_list = reversed_list.next

    print 'Reversed list by position {}\{} is {}'.format(m, n, result)

