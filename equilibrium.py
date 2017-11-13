#!/usr/bin/env python
"""
Equilibrium index of an array is an index such that the sum of elements at lower indexes is equal to
the sum of elements at higher indexes. For example, in an array A:

A[0] = -7, A[1] = 1, A[2] = 5, A[3] = 2, A[4] = -4, A[5] = 3, A[6]=0

3 is an equilibrium index, because:
A[0] + A[1] + A[2] = A[4] + A[5] + A[6]

6 is also an equilibrium index, because sum of zero elements is zero, i.e., A[0] + A[1] + A[2] + A[3] + A[4] + A[5]=0

7 is not an equilibrium index, because it is not a valid index of array A.

Solution:

1) Initialize leftsum  as 0

2) Get the total sum of the array as sum

3) Iterate through the array and for each index i, do following.
    a)  Update sum to get the right sum.
           sum = sum - arr[i]         // sum is now right sum
    b) If leftsum is equal to sum, then return current index.
    c) leftsum = leftsum + arr[i]     // update leftsum for next iteration.

4) return -1 // If we come out of loop without returning then
             // there is no equilibrium index

Time Complexity: O(n)
"""


def equilibrium(nums):
    if not nums:
        return -1

    sum_total = sum(nums)    # initialize sum of whole array
    left_sum = 0             # initialize leftsum

    for i, num in enumerate(nums):
        sum_total -= num     # sum is now right sum for index i

        if left_sum == sum_total:
            return i

        # update left sum
        left_sum += num

    # no equilibrium
    return -1

if __name__ == '__main__':
    nums = [-7, 1, 5, 2, -4, 3, 0]
    print equilibrium(nums)
