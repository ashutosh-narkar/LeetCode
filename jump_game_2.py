#!/usr/bin/env python
'''
Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.
Your goal is to reach the last index in the minimum number of jumps.

For example:
Given array A = [2,3,1,1,4]

The minimum number of jumps to reach the last index is 2. (Jump 1 step from index 0 to 1, then 3 steps to the last index.)
'''
def jump(A):
    if not A:
        return 0

    last = 0
    curr = 0
    steps = 0

    for i in range(len(A)):
        # if the distance travelled upto "current index" exceeds the last distance travelled
        if i > last:
            # if not last one and can't go further
            if curr == last and last < len(A) - 1:
                return -1    # never reach the last one

            last = curr
            steps += 1

        # Why "i + A[i]" ? The distance travelled (ie. index that can be reached from current position) is sum of "the jump at that position + index of the position"
        curr = max(curr, i + A[i])

    return steps



##########################################################
'''
Use this solution
'''

def jump(A):

    if len(A) <= 1:
        return 0

    m = 0
    steps = 0
    i = 0

    while i < len(A):

        m = max(m, i + A[i])

        if m > 0:
            steps += 1

        # end
        if m >= len(A) - 1:
            return steps

        # iterate though all positions we can jump from where we standing, 
        # find the largest i + A[i] (greedy) and jump to that index.        
        tmp = 0
        for j in range(i + 1, m + 1):
            if (j + A[j]) > tmp:
                tmp = j + A[j]
                i = j

    return steps


if __name__ == '__main__':
    data  = [2, 3, 1, 1, 4]
    print 'Min steps to reach last index in {} is {}'.format(data, jump(data))


    data  = [3, 2, 1, 0, 4]
    print 'Min steps to reach last index in {} is {}'.format(data, jump(data))
