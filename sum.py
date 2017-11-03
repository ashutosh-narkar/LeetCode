#!/usr/bin/env python
'''
Recursive method to find sum of array of integers
'''
def sum_rec(numbers):
    # empty list has sum = 0
    if not numbers:
        return 0 

    if len(numbers) == 1:
        return numbers[0]

    return sum_rec(numbers[1:]) + numbers[0]


if __name__ == '__main__':
    data = []
    assert sum(data) == sum_rec(data)
    print sum_rec(data)
