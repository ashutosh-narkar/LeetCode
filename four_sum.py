#!/usr/bin/env python
'''
Given an array S of n integers, are there elements a, b, c, and d in S such that a + b + c + d = target? 
Find all unique quadruplets in the array which gives the sum of target.

Note:
1) Elements in a quadruplet (a,b,c,d) must be in non-descending order. (ie, a <= b <= c <= d)
2) The solution set must not contain duplicate quadruplets.

For example, given array S = {1 0 -1 0 -2 2}, and target = 0.

    A solution set is:
    (-1,  0, 0, 1)
    (-2, -1, 1, 2)
    (-2,  0, 0, 2)
'''

# @return a list of lists of length 4, [[val1,val2,val3,val4]]

def fourSum(self, num, target):
	if len(num) <  4:
		return []

	result = set()

	# since numbers must be in non-descending order
	num.sort()

	for i in range(len(num) -3):
		for j in  range(i + 1, len(num) -2):

			desired = target - num[i] - num[j]
			start = j + 1
			end = len(num) - 1
	    

			while start < end:
				if num[start] + num[end] == desired:
					res = (num[i], num[j], num[start], num[end])

					if res not in result:
						result.add(res)
						start += 1
						end -= 1


					elif num[start] + num[end] < desired:
						start += 1

					else:
						end -= 1

		    
	# return value is list of lists
	result = map(list, result)

	return list(result)

		
