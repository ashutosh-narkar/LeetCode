#!/usr/bin/env python
'''
Given a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list.

For example,
Given 1->2->3->3->4->4->5, return 1->2->5.
Given 1->1->1->2->3, return 2->3.
'''

class ListNode:
	def __init__(self, x):
		self.val = x
		self.next  = None

def deleteDuplicates(self, head):

	if not head:
		return

	count  = {}
	current = head
    
	#  count occurences of values
	while current:
		if current.val in count:
			count[current.val] += 1
		else:
			count[current.val] = 1

		current = current.next

	
	# create a temp node and make it new head. This may
	# be needed if head is to be removed
	p = ListNode(0)
	p.next = head
	head = p
	current = p

	while current.next:
		# if only one instance
		if count[current.next.val] == 1:
			current = current.next

		# multiple instances
		else:
			temp = current
			# after this loop, temp will point to last instance of duplicate node
			for i in range(count[current.next.val]):
				temp = temp.next
			current.next = temp.next

	return p.next
