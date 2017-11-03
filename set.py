#!/usr/bin.env python
'''
Design a data structure that supports all following operations in average O(1) time.

insert(val): Inserts an item val to the set if not already present.
remove(val): Removes an item val from the set if present.
getRandom: Returns a random element from current set of elements. Each element must have the same probability of being returned.

OR

Design a set data structure in Python
'''


import random
class RandomizedSet(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """

        # List holds the numbers
        # Dict holds the numbers and its index in the list
        self.nums = list()
        self.pos = dict()

    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.pos:
            return False

        self.nums.append(val)
        self.pos[val] = len(self.nums) - 1
        return True

    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val not in self.pos:
            return False

        # swap the number to be removed with the last number in the list and then pop the list
        index = self.pos[val]
        last = len(self.nums) - 1
        self.nums[index], self.nums[last] = self.nums[last], self.nums[index]

        self.pos[self.nums[index]] = index

        del self.pos[val]
        self.nums.pop()

        return True

    def getRandom(self):
        """
        Get a random element from the set.
        :rtype: int
        """
        return self.nums[random.randint(0, len(self.nums) - 1)]

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()

