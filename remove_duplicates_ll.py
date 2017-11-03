#!/usr/bin/env python
'''
Write a removeDuplicates() function which takes a list 
and deletes any duplicate nodes from the list. The list is not sorted.

For example if the linked list is 12->11->12->21->41->43->21 
then removeDuplicates() should convert the list to 12->11->21->41->43.
'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def add(self, data):
        node = Node(data)
        if not self.head:
            self.head = node
        else:
            node.next = self.head
            self.head = node

def create_singly_ll(nodes):
    ll = LinkedList()

    for node in nodes:
        ll.add(node)

    # return head
    return ll.head


def removeDuplicates(head):
    if not head:
        return

    current = head
    visited = []
    visited.append(current.data)
  
    while current.next:
        if current.next.data not in visited:
            visited.append(current.next.data)
            current = current.next

        # duplicate found
        else:
            current.next = current.next.next

    return visited


def print_ll(head):
    if not head:
        return

    current = head
    while current:
        print current.data
        current = current.next



if __name__ == '__main__':
    ll_head = create_singly_ll([21, 43, 41, 12, 12, 11, 12])

    print 'Original list'
    print_ll(ll_head)

    print '\n'

    res = removeDuplicates(ll_head)
    res.reverse()
    ll_head_no_dups = create_singly_ll(res)  
  
    print 'Duplicates removed'
    print_ll(ll_head_no_dups)

