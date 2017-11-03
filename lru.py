#!/usr/bin/env python
'''
Design and implement a data structure for Least Recently Used (LRU) cache.
It should support the following operations: get and set.

get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
set(key, value) - Set or insert the value if the key is not already present.
When the cache reached its capacity, it should invalidate the least recently used item before inserting a new item.

Solution:
Maintain a dict to store the cache items. Dict has the form {key: (value, node)}

Maintain a doubly link list to keep track of usage. Nodes at the beginning of the list are most recently used.
This means a node at list end is least recently used.

The value of each node is the key that is to be set/get.

'''

class ListNode:

    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None


class LRUCache:

    # @param capacity, an integer

    def __init__(self, capacity):

        self.capacity = capacity
        
        # to store the key-val pairs 
        self.cache = {}

        self.head = ListNode(-1)
        self.tail = ListNode(-1)

        self.head.next = self.tail
        self.tail.prev = self.head



    # @return an integer
    def get(self, key):

        if key not in self.cache:
            return -1

        result, node = self.cache[key]

        # Move node to beginning of list
        node.prev.next = node.next
        node.next.prev = node.prev
        self.insertFront(node)

        return result

        
        

    # @param key, an integer
    # @param value, an integer
    # @return nothing
    def set(self, key, value):

        # case1: key already exists

        if key in self.cache:
            val, node = self.cache[key]

            # Move node to beginning of list
            node.prev.next = node.next
            node.next.prev = node.prev
            self.insertFront(node)

            # update cache value
            self.cache[key] = (value, node)

        # case2: key not present
        else:
       
            # add key
            if len(self.cache) < self.capacity:

                # create a node and insert at front of list
                # add key to cache
                node = ListNode(key)
                self.insertFront(node)
                self.cache[key] = (value, node)

            # remove least recently used key and add new key
            else:

                # node before tail is least recently used
                node = self.tail.prev

                # remove key from cache
                del self.cache[node.val]

                # update node val and move to beginning of list
                # add key to cache
                node.val = key
                
                node.prev.next = node.next
                node.next.prev = node.prev
                self.insertFront(node)
 
                self.cache[key] = (value, node)

    def insertFront(self, node):
        node.next = self.head.next
        self.head.next.prev = node

        node.prev = self.head
        self.head.next = node