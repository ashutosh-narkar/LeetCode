#!/usr/bin/env python
'''

LOOK AT remove_duplicates_array_2.py

Follow up for "Remove Duplicates"
What if duplicates are allowed at most twice?

For example,
Given sorted array A = [1,1,1,2,2,3],

Your function should return length = 5, and A is now [1,1,2,2,3].
'''


def removeDuplicates(A):

	if not A or len(A) <= 1:
		return A

	count = {}
	for num in A:
		if num not in count:
			count[num]  = 1
		else:
			count[num] += 1


	result = []
	for num, _count in count.items():
		if _count < 2:
			result.append(num)
		else:
			result.append(num)
			result.append(num)


	return len(result)

if __name__ == '__main__':
    input = [1,1,1,2,2,3]

    print removeDuplicates(input) 
