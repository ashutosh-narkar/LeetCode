#!/usr/bin/env python
'''
Given an array that contains both positive and negative integers, find the product of the maximum product subarray. 
Expected Time complexity is O(n) and only O(1) extra space can be used
'''
def max_product(numbers):
    if not numbers:
        return 

    max_prod = numbers[0]
    max_pos = numbers[0]
    max_neg = numbers[0]

    for i in numbers[1:]:
        if i == 0:
            max_pos = 0
            max_neg = 0

        elif i > 0:
            max_pos = max(max_pos * i, i)
            max_neg *= i

        else:
            temp = max_pos
            max_pos = i * max_neg
            max_neg = min(temp * i, i)

        max_prod = max(max_pos, max_prod)

    return max_prod


if __name__ == '__main__':

    # Test Cases
    data = [6, 3, 10, 0, 2]
    assert max_product(data) == 180

    data = [2, 3, -2, 4]
    assert max_product(data) == 6

    data = [1, -3, -10, 0, 60]
    assert max_product(data) == 60

    data = [-2, -3, 0, -2, -40]
    assert max_product(data) == 80

    data = [12, 2, -3, -5, -6, -2]
    assert max_product(data) == 4320     

    data = [1, -2, -3, 0, 7, -8, -2]
    assert max_product(data) == 112

    print 'Tests passed'
