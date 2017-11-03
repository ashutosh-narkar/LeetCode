#!/usr/bin/env python
'''
Given a linked list, return the node where the CYCLE BEGINS. If there is no cycle, return null.

Solution:
Using a fast pointer that advances two nodes each time and a slow pointer that advances on node, we always detect a cycle as the fast pointer cannot overtake the slow one withoutbeing in the same node in one of the ``turns".

'''

def detectCycle(head):
    if not head:
        return

    slow = head
    fast = head
    
    while slow and fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            slow = head
            while slow != fast:
                slow = slow.next
                fast = fast.next

            return slow

    return





###### If we only have to return if there is a cycle or not

def hasCycle(head):
    if not head:
        return False

    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            return True

    return False





