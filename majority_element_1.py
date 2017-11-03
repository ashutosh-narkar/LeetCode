#!/usr/bin/env python
'''
Given an array of size n, find the majority element. 
The majority element is the element that appears more than [ n/2 ] times.

You may assume that the array is non-empty and the majority element always exist in the array.

Analysis:
Moore voting algorithm: We maintain a current candidate and a counter initialized to 0. As we iterate the array, we look at the current element x:
1) If the counter is 0, we set the current candidate to x and the counter to 1.
2) If the counter is not 0, we increment or decrement the counter based on whether x is the current candidate.

After one pass, the current candidate is the majority element. Runtime complexity = O(n).

'''


def majorityElement(num):
        
	majority = num[0]
	counter = 1

	for n in num[1:]:
		if n == majority:
			counter += 1

		else:
			counter -= 1

		if counter == 0:
			majority = n
			counter = 1

	return majority

