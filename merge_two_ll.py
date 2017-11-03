#!/usr/bin/env python
'''
Merge two sorted linked lists and return it as a new list. 
The new list should be made by splicing together the nodes of the first two lists.
'''
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


def mergeTwoLists(l1, l2):
    
    # create a dummy node
    res = ListNode(0)
    current = res

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

    # since res is a dummy node
    return res.next 

if __name__ == '__main__':

    # list 1
    n1 = ListNode(1)
    n2 = ListNode(3)
    n3 = ListNode(5)

    n1.next = n2
    n2.next = n3

    # list 2
    n4 = ListNode(2)
    n5 = ListNode(4)
    n6 = ListNode(6)

    n4.next = n5
    n5.next = n6


    print 'Original lists 1 -> 3 -> 5 and 2 -> 4 -> 6'
    merged = mergeTwoLists(n1,  n4)

    result = ''
    while merged:
        result += str(merged.val) + ' -> '
        merged = merged.next


    print 'Merged List {}'.format(result)












 
