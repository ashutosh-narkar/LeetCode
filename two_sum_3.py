#!/usr/bin/env python
'''
Design and implement a TwoSum class. It should support the following operations: add and find.

add - Add the number to an internal data structure.
find - Find if there exists any pair of numbers which sum is equal to the value.

For example,
add(1); add(3); add(5);

find(4) -> true
find(7) -> false
'''
class TwoSum:
    def __init__(self):
        self.table = {}

    def add(self, num):
        if num in self.table:
            self.table[num] += 1
        else:
            self.table[num] = 1

    def find(self, target):
        for num in self.table.values():
            desired = target - num

            if desired != num and desired in self.table:
                return True

            elif desired == num and self.table[num] > 1:
                return True

        return False


if __name__ == '__main__':
    obj = TwoSum()

    obj.add(1)
    obj.add(2)
    obj.add(3)

    print obj.find(4)
    print obj.find(7)
