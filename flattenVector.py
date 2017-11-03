#!/usr/bin/env python
'''
Implement an iterator to flatten a 2d vector.
For example,
Given 2d vector =
[
  [1,2],
  [3],
  [4,5,6]
]
By calling next repeatedly until hasNext returns false, the order of elements returned by next should be: [1,2,3,4,5,6].
'''


class Vector2D:
    # Initialize your data structure here.
    # @param {integer[][]} vec2d
    def __init__(self, vec2d):
        self.col = 0
        self.row = 0
        self.vec = vec2d

    # @return {integer}
    def next(self):
        result = self.vec[self.row][self.col]
        self.col += 1
        return result

    # @return {boolean}
    def hasNext(self):
        while self.row < len(self.vec):
            if self.col < len(self.vec[self.row]):
                return True

            self.col = 0
            self.row += 1

        return False


def test():
    vector = [[4,3], [2,4,5], [], [4,5,6]]

    x = Vector2D(vector)

    result = []
    while x.hasNext():
        result.append(x.next())

    print result

if __name__ == '__main__':
    test()