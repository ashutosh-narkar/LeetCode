#!/usr/bin/env python
'''
Given a sorted integer array where the range of elements are [0, 99] inclusive, return its missing ranges.
For example, given [0, 1, 3, 50, 75], return ['2', '4->49', '51->74', '76->99']

Runtime: O(n)
'''
def missing_range(nums, lower, upper):
    
    missing_ranges = []

    if not nums:
        full_range = str(lower) + '->' + str(upper)
        missing_ranges.append(full_range)
        return missing_ranges

    # first missing range
    if nums[0] > lower:
        first_range = str(lower) + '->' + str(nums[0] - 1)
        missing_ranges.append(first_range)

    for i, j in zip(nums[:-1], nums[1:]):

        # no missing
        if j - i == 1:
            continue

        # single number missing
        elif j - i == 2:
            missing_ranges.append(str(i + 1))

        # range missing
        else:
            miss_range = str(i + 1) + '->' + str(j - 1)
            missing_ranges.append(miss_range)


    # last missing range
    if nums[-1] <  upper:
        last_range = str(nums[-1] +  1) + '->' + str(upper)
        missing_ranges.append(last_range)

    return missing_ranges 


if __name__ == '__main__':
    #nums = [3, 6, 7, 8, 10, 50, 100, 122, 123]
    #lower = 0
    #upper = 123

    nums = []
    lower = 1
    upper = 1 

    print 'Input {} Lower {} Upper {}'.format(nums, lower, upper)
    print 'Missing Range {}'.format(missing_range(nums, lower, upper))
