#!/usr/bin/env python
'''
**** FOR SORTING A LL USING MERGE SORT LOOK AT sort_ll_1.py ****

Sort a linked list in O(n log n) time using constant space complexity.

Algorithm: Bottom-up Merge Sort
http://algs4.cs.princeton.edu/22mergesort/
'''


class Solution(object):
    def sortList(self, head):
        if not head or not head.next:
            return head

        current = head
        length = 0
        while current:
            length += 1
            current = current.next

        step = 1  # length of sorted sublists: at first we start with 1
        while step < length:  # if greater than len, we have the whole list sorted
            head = self.mergeLayer(head, step)
            step *= 2  # each iterate double the length of sorted sublists

        return head

    # merge every two sublists of length lenOfList, assuming each sublist is already sorted
    def mergeLayer(self, head, lenOfList):
        fakehead = ListNode(0)
        merge_tail = fakehead  # merge_tail points to the tail of merged part of this layer
        while head:
            first = head
            first_tail = self.getListTail(first, lenOfList)
            second = first_tail.next
            if not second:  # we have only 1 sorted sublist,
                merge_tail.next = head  # link the sorted part to the last sorted sublist
                break
            second_tail = self.getListTail(second, lenOfList)
            head = second_tail.next  # now we have get two suitable subllists, point head to the rest

            first_tail.next = None
            second_tail.next = None
            pair = self.merge(first, second)
            merge_tail.next = pair[0]  # link the old sorted part to the newly sorted part
            merge_tail = pair[1]  # update the end of sorted part

        return fakehead.next

    # get the tail of the list with head 'head' and length 'len' (or at most len)
    def getListTail(self, head, length):
        while length > 1 and head.next:
            head = head.next
            length -= 1
        return head

    # merge two sorted lists, return both the head and tail of the new list
    def merge(self, l1, l2):
        fakehead = ListNode(0)
        tail = fakehead
        while l1 and l2:
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next
        tail.next = l2 if not l1 else l1
        while tail.next:
            tail = tail.next
        return fakehead.next, tail
