#!/usr/bin/env python
'''
Given a singly linked list, determine if it is a palindrome.

Solution:
1) Find the center of the ll
2) Reverse the ll from the center to the end
3) Now compare the original ll from beginning to center and the revrsed ll from center to end

Time  O(n)
Space O(1)
'''



def isPalindrome(head):
    """
    :type head: ListNode
    :rtype: bool
    """
    if not head:
        return True

    slow, fast = head, head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    head1 = slow
    last = None
    current = head1

    while current:
        next = current.next
        current.next = last
        last = current
        current = next

    head1 = last

    while head and head1:
        if head.val != head1.val:
            return False

        head = head.next
        head1 = head1.next

    return True
