#!/usr/bin/env pyhton
"""
Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.
If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).

The replacement must be in-place, do not allocate extra memory.

Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.
1,2,3 -> 1,3,2
3,2,1 -> 1,2,3
1,1,5 -> 1,5,1

Analysis:
From the Wikipedia, one classic algorithm to generate next permutation is:

Step 1: Find the largest index k, such that A[k] < A[k+1]. If no such index exists, the permutation
is sorted in descending order, just reverse it to ascending order and we are done.

For example, the next permutation of [3, 2, 1] is [1, 2, 3].

Step 2: Find the largest index l greater than k such that A[k] < A[l].

Step 3: Swap A[k] and A[l].

Step 4: Reverse A[k+1] to the end
"""

# @param num, a list of integer
# @return nothing (void), do not return anything, modify num in-place instead.


def next_permutation(num):

    k, l = -1, -1

    # step 1
    for i in range(len(num) - 1):
        if num[i] < num[i + 1]:
            k = i

    if k == -1:
        num.reverse()
        return

    # step 2
    for i in range(k + 1, len(num)):
        if num[i] > num[k]:
            l = i

    # step 3
    num[l], num[k] = num[k], num[l]

    # step 4
    num[k+1: len(num): 1] = num[len(num) -1: k: -1]        # very cool
