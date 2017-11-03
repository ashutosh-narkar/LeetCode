#!/usr/bin/env python
'''
Given two arrays: arr1[0..m-1] and arr2[0..n-1]. Find whether arr2[] is a subset of arr1[] or not.
Both the arrays are not in sorted order.

Time Complexity: O(mLogm + nLogn)
Method will handle duplicates
'''


def isSubset(arr1, arr2):
    if not (arr1 or arr2):
        return True

    if not arr1 or not arr2:
        return False

    arr1.sort()
    arr2.sort()

    m, n = 0, 0

    while m < len(arr1) and n < len(arr2):
        if arr1[m] == arr2[n]:
            m += 1
            n += 1

        elif arr1[m] < arr2[n]:
            m += 1

        # since element of array2 is smaller, he cannot be in array1
        else:
            return False

    if n == len(arr2):
        return True

    return False


if __name__ == '__main__':
    
    res = isSubset([11, 1, 13, 21, 3, 7], [11, 3, 7, 1])
    assert res == True

    res = isSubset([1, 2, 3, 4, 5, 6], [1, 3, 4])
    assert res == True

    res = isSubset([10, 5, 2, 23, 19], [19, 5, 3])
    assert res == False

    res = isSubset([1, 4, 2], [1, 4, 4, 2])
    assert res == False

    print 'Tests passed'
