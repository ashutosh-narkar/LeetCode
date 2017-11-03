#!/usr/bin/env python
'''
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
getMin() -- Retrieve the minimum element in the stack.
'''

class Node:

    def __init__(self, val):
        self.val = val
        self.next = None


class MinStack:
    # @param x, an integer
    # @return an integer

    def __init__(self):
        self.head = Node(float('inf'))
    
    def push(self, x):

        # push new element after head
        node = Node(x)
        node.next = self.head.next
        self.head.next = node


        # update new element being pushed has smaller val than head, then update head's val
        if self.head.val > x:
            self.head.val = x


    # @return nothing
    def pop(self):

        # since we insert new values at beginning of list, we simply
        # remove element after head
        if not self.head.next:
            return


        node = self.head.next
        self.head.next = node.next


        # if element that is to be removed had the minimum val
        # we need to find next min val and update head's val
        if node.val == self.head.val:
            current = self.head.next
            self.head.val = float('inf')  # reset head's val

            while current:
                if current.val < self.head.val:
                    self.head.val = current.val
                current = current.next
            

        return
        

    # @return an integer
    def top(self):

        if not self.head.next:
            return

        return self.head.next.val


    # @return an integer
    def getMin(self):
        if not self.head.next:
            return
        return self.head.val
