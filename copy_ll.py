#!/usr/bin/env python
'''
A linked list is given such that each node contains an additional random pointer 
which could point to any node in the list or null.

Return a deep copy of the list.

Solution:

1) Create the copy of node 1 and insert it between node 1 & node 2 in original Linked List, 
create the copy of 2 and insert it between 2 & 3.. Continue in this fashion, add the copy of N after the Nth node


2) Now copy the arbitrary link in this fashion
      original->next->arbitrary = original->arbitrary->next;
This works because original->next is nothing but copy of original and Original->arbitrary->next is nothing but copy of arbitrary.

3) Now restore the original and copy linked lists in this fashion in a single loop.

     original->next = original->next->next;
     copy->next = copy->next->next;

Time Complexity: O(n)
Auxiliary Space: O(1)

'''


# Definition for singly-linked list with a random pointer.
# class RandomListNode(object):
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None

class Solution(object):
	def copyRandomList(self, head):
		"""
        :type head: RandomListNode
        :rtype: RandomListNode
        """
		if not head:
			return

		# Step 1 - Create nodes
		current = head

		while current:
			node = RandomListNode(current.label)
			next = current.next
			current.next = node
			node.next = next

			current = current.next.next

		# Step 2 - Adjust Random pointers
		current = head

		while current:
			if current.random:
				current.next.random = current.random.next

			current = current.next.next

		# Step 3 - Separate the lists
		original = head
		copy = head.next

		while original and original.next:
			next = original.next
			original.next = next.next
			original = next

		return copy





def printList(node):
    if not node:
        return

    current = node

    while current:
        print current.label
        current = current.next


if __name__ == '__main__':
    
    node1 = RandomListNode('1')
    node2 = RandomListNode('2')
    node3 = RandomListNode('3')

    node1.next = node2
    node1.random = node2

    node2.next = node3
    node2.random = node3
  

    newList = copyRandomList(node1)
 
    print 'Original List'
    printList(node1)

    print 'Copied List'
    printList(newList)





