#!/usr/bin/env python
'''
Implement a queue API using an array for storing elements. Your
API should include a constructor function, which takes as argument the capacity of the queue,
enqueue and dequeue functions, a size function, which returns the number of elements
stored, and implement dynamic resizing.


Solution:
We use an array of length n to store up to n elements. We resize the
array by a factor of 2 each time we run out of space. The queue has a head field that
indexes the least recently inserted element, and a tail field, which is the index that
the next inserted element will be written to. We record the number of elements in
the queue with a count variable. Initially, head and tail are 0. When count = n and
a enqueue is attempted we resize. When count = 0 and a dequeue is attempted we
throw an exception.

The time complexity of each operation is O(1)

'''


class Queue:
    def __init__(self, capacity):
        self.capacity = capacity

        self.items = [None] * self.capacity
    
        self.head, self.tail = 0, 0
        self.count = 0

    def getSize(self):
        return self.count

    def dequeue(self):
        if not self.items:
            raise Exception('empty queue')

        self.count -= 1

        data = self.items[self.head]
        head = (self.head + 1) % len(self.items)

        return data

    def enqueue(self, item):

        if len(self.items) == self.capacity:
 
            # Dynamically resizes array as limit reached limit

            # Rearange elements
            self.items = self.items[self.head: self.tail]
         
            # reset head and tail
            self.head = 0
            self.tail = self.count

            # resize array
            temp = [None] * len(self.items)
            self.items.extend(temp)

        # perform enque   
        self.items[self.tail] = item
        tail = (self.tail + 1) % len(self.items)
        self.count += 1

    
