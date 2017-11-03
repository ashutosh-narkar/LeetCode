#!/usr/bin/env python
'''
You are given two linked lists representing two non-negative numbers. 
The digits are stored in reverse order and each of their nodes contain a single digit. 
Add the two numbers and return it as a linked list.

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
'''

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


def add_two_numbers(l1, l2):
    carry = 0

    # create dummy node for result list
    dummy = ListNode(0)
    current = dummy

    while l1 or l2:
        num1, num2 = 0, 0

        if l1:
            num1 = l1.val
            l1 = l1.next

        if l2:
            num2 = l2.val
            l2 = l2.next

        num = num1 + num2 + carry

        carry = num / 10
        num = num % 10

        node = ListNode(num)
        current.next = node
        current = current.next

    # final carry
    if carry > 0:
        node = ListNode(carry)
        current.next = node

    return dummy.next
