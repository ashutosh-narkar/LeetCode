#!/usr/bin/env python
'''
Write a program to find the node at which the intersection of two singly linked lists begins.

Runtime: O(n) 
Memory:  O(1)

Solution:
1) Get count of the nodes in first list, let count be c1.
2) Get count of the nodes in second list, let count be c2.
3) Get the difference of counts d = abs(c1 - c2)
4) Now traverse the bigger list from the first node till 'd' nodes so that from here onwards both the lists have equal no of nodes.
5) Then we can traverse both the lists in parallel till we come across a common node.
(Note that getting a common node is done by comparing the address of the nodes)

'''


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def getIntersectionNode(headA, headB):
    if headA and not headB or headB and not headA or not (headA or headB):
        return

    currA, currB = headA, headB
    lenA, lenB = 0, 0

    while currA:
        lenA += 1
        currA = currA.next

    while currB:
        lenB += 1
        currB = currB.next

    currA,currB = headA, headB

    if lenA > lenB:
        for i in range(lenA - lenB):
            currA = currA.next

    elif lenB > lenA:
        for i in range(lenB - lenA):
            currB = currB.next

    while currA and currB:
        if currA == currB:
            return currA
        currA = currA.next
        currB = currB.next

    return

if __name__ == '__main__':
    node1_1 = ListNode(3)
    node2_1 = ListNode(6)
    node3_1 = ListNode(9)
    node4_1 = ListNode(15)
    node5_1 = ListNode(30)

    node1_1.next = node2_1
    node2_1.next = node3_1
    node3_1.next = node4_1
    node4_1.next = node5_1


    node1_2 = ListNode(10)
    node2_2 = node4_1
    node3_2 = node5_1

    node1_2.next = node2_2
    node2_2.next = node3_2


    
    print 'Intersection point is {}'.format(getIntersectionNode(node1_1, node1_2).val)


























