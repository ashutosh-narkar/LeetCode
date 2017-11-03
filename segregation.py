#!/usr/bin/env python
'''
Given an array A[], write a function that segregates even and odd numbers.
The functions should put all even numbers first, and then odd numbers.
'''

def segregation(numbers):
    if not numbers:
        raise ValueError('No input')

    left = 0
    right = len(numbers) - 1

    while left < right:
        
        while left < len(numbers) and not numbers[left] % 2:
            left += 1

        while right >= 0 and numbers[right] % 2:
            right -= 1

        if left < right:
            numbers[left], numbers[right] = numbers[right], numbers[left]
            left += 1
            right -= 1

    return numbers

if __name__ == '__main__':
    data = [3, 6, 7, 0, 2 ,10, 13, 14, 5, 12, 1]
    print 'Original: {}'.format(data)
    res = segregation(data)

    print 'Ordered: {}'.format(res)
