#!/usr/bin/env python
"""
Programming Assignment - 1
Compute the number of inversions, given 100000 non-repeated integers.
Use mergesort to sort the integers

What are inversions ?
Inversion Count for an array indicates - how far (or close) the array is from being sorted.
If array is already sorted then inversion count is 0.
If array is sorted in reverse order that inversion count is the maximum.

Formally speaking, two elements a[i] and a[j] form an inversion if a[i] > a[j] and i < j

"""

import os
FILE_PATH = os.path.expanduser('~/coursera/algorithms1/week1/IntegerArray.txt')
inversions = 0


def read_data(path):
    '''
    Read the file data containing the integers
    '''
    numbers = []
    with open(path) as f:
        lines = f.readlines()
        for line in lines:
            numbers.append(int(line))
    return numbers


def merge(left, right):
    '''
    Implement merge step of mergesort
    '''
    result = []
    n, m = 0, 0

    while n < len(left) and m < len(right):
        if left[n] <= right[m]:
            result.append(left[n])
            n += 1
        else:
            result.append(right[m])
            m += 1
            global inversions
            inversions += len(left[n:])

    result.extend(left[n:])
    result.extend(right[m:])
    return result


def sort(seq):
    '''
    Implement divide step of mergesort
    '''
    if len(seq) <= 1:
        return seq

    middle = len(seq) / 2
    left = sort(seq[:middle])
    right = sort(seq[middle:])
    return merge(left, right)


def main():
    '''
    Return the number of inversions
    '''
    #data = read_data(FILE_PATH)
    data = [1, 20, 6, 4, 5]
    result = sort(data)
    print 'Number of inversions {}'.format(inversions)


if __name__ == '__main__':
    main()
