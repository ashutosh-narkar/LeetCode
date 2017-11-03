#!/usr/bin/env python
'''
Merge k sorted linked lists and return it as one sorted list.

Time: log(k) * n.
k is number of list and n is number of total elements.
'''

from heapq import heappop, heappush

class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

def mergeKLists(lists):

    if not lists:
        return

    # create a dummy node
    res = ListNode(0)
    current = res

    # get a list of tuples so that we can put them in a heap based on node's val
    heap =[]
    for item in lists:
        if item:
            heappush(heap, (item.val, item))

    while heap:
        current.next = heappop(heap)[1]
        current = current.next
        
        # keep adding next element of each list 
        if current.next:
            heappush(heap, (current.next.val, current.next))

    return res.next

if __name__ == '__main__':

    # list 1
    n1 = ListNode(1)
    n2 = ListNode(5)
    n3 = ListNode(9)

    n1.next = n2
    n2.next = n3

    # list 2
    n4 = ListNode(2)
    n5 = ListNode(4)
    n6 = ListNode(10)

    n4.next = n5
    n5.next = n6

    # list 3
    n7 = ListNode(3)
    n8 = ListNode(7)

    n7.next = n8


    print 'Original lists 1 -> 5 -> 9, 2 -> 4 -> 10 and 3 -> 7'
    merged = mergeKLists([n1,  n4, n7])

    result = ''
    while merged:
        result += str(merged.val) + ' -> '
        merged = merged.next


    print 'Merged List {}'.format(result)
 
