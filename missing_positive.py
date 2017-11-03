#!/usr/bin/env python
'''
Given an unsorted integer array, find the first missing positive integer.

For example,
Given [1,2,0] return 3,
and [3,4,-1,1] return 2.

Your algorithm should run in O(n) time and uses constant space.
'''


def firstMissingPositive(A):

	if not A:
		return 1
	
	# insert a dummy value otherwise cases like [1] will fail
	A.insert(0, 0)

	n = len(A)

	#Pass 1, move every value to the position equal to its value
	for i in range(n):
		target = A[i]
		while 0 <= target < n and target != A[target]:  # ignore negative values
			new_target = A[target]
			A[target] = target
			target = new_target

	#Pass 2, find first location where the index doesn't match the value
	for i in range(n):
		if i != A[i]:
			return i

	return n

