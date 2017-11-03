#!/usr/bin/env python
'''
An Array of integers is given, both +ve and -ve. You need to find the two elements such that their sum is closest to zero.

eg [1, 60, -10, 70, -80, 85] return -80 and 85
'''
def twoSumClosest(num, target):
    if not num:
        return 

    num.sort()

    i, j = 0, len(num) - 1

    result = None
    min_diff = float('inf')

    while i < j:
        current_sum = num[i] + num[j]
        if current_sum == target:
            result = (num[i], num[j])
            break

        diff = abs(target - current_sum)
        if diff < min_diff:
            min_diff = diff
            result = (num[i], num [j])

        if current_sum < target:
            i += 1
                
        else:
            j -= 1


    return result

if __name__ == '__main__':
    print twoSumClosest([1, 60, -10, 70, -80, 85], 0)
