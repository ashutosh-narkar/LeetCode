#!/usr/bin/env python
"""
Design and implement a data structure for Least Frequently Used (LFU) cache.
It should support the following operations: get and put.

get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
put(key, value) - Set or insert the value if the key is not already present.
When the cache reaches its capacity, it should invalidate the least frequently used item before inserting a new item.
For the purpose of this problem, when there is a tie (i.e., two or more keys that have the same frequency),
the least recently used key would be evicted.

Follow up:
Could you do both operations in O(1) time complexity?

Solution:
Maintain 2 maps and 1 doubly linked list

-> cache map is of form {key -> (value, node, freq)}
-> freq map is of form {key -> Linked List Object}
-> Maintain a doubly linked list similar to lru cache

"""


class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None


class LinkedList:
    def __init__(self):
        self.head = ListNode(-1)
        self.tail = ListNode(-1)

        self.head.next = self.tail
        self.tail.prev = self.head

    def addNodeInFront(self, node):
        node.next = self.head.next
        self.head.next.prev = node

        node.prev = self.head
        self.head.next = node

    def removeNode(self, node):
        node.next.prev = node.prev
        node.prev.next = node.next

    def removeLastNode(self):
        node = self.tail.prev
        self.removeNode(node)
        return node

    def isAnyNode(self):
        if self.head.next == self.tail and self.tail.prev == self.head:
            return False

        return True


class LFUCache(object):
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.cap = capacity

        self.cache = {}

        self.freqNodes = {}

        self.minfreq = 1

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.cache:
            return -1

        value, node, freq = self.cache[key]

        linkedList = self.freqNodes[freq]
        linkedList.removeNode(node)

        freq += 1
        if freq not in self.freqNodes:
            linkedList = LinkedList()
        else:
            linkedList = self.freqNodes[freq]

        linkedList.addNodeInFront(node)
        self.freqNodes[freq] = linkedList

        linkedList = self.freqNodes[self.minfreq]
        if not linkedList.isAnyNode():
            self.minfreq += 1

        return value

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if key in self.cache:
            val, node, freq = self.cache[key]

            linkedList = self.freqNodes[freq]
            linkedList.remove(node)

            freq += 1
            if freq not in self.freqNodes:
                linkedList = LinkedList()
            else:
                linkedList = self.freqNodes[freq]

            linkedList.addNodeInFront(node)

            self.freqNodes[freq] = linkedList
            self.cache[key] = (value, node, freq)

        else:
            if self.cap == 0:
                return

            if len(self.cache) >= self.cap:
                linkedList = self.freqNodes[self.minfreq]
                removedNode = linkedList.removeLastNode()

                del self.cache[removedNode.val]

            node = ListNode(key)

            freq = 1
            self.cache[key] = (value, node, freq)

            if freq not in self.freqNodes:
                linkedList = LinkedList()

            else:
                linkedList = self.freqNodes[freq]

            linkedList.addNodeInFront(node)

            self.freqNodes[freq] = linkedList
            self.minfreq = 1


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

if __name__ == '__main__':
    capacity = 2
    obj = LFUCache(capacity)
    print obj.put(1, 1)
    print obj.put(2, 2)
    print obj.get(1)
    print obj.put(3, 3)
    print obj.get(2)