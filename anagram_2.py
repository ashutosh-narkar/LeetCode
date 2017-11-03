#!/usr/bin/env python
'''
Given an array of strings, return all groups of strings that are anagrams.
Note: All inputs will be in lower-case.
'''

'''
Solution 1:
Two strings are anagrams if and only if their character counts (respective number of occurrences of each character) are the same.

Complexity Analysis

Time Complexity: O(N * K) where N is the length of strs, and K is the maximum length of a string in strs. 
Counting each string is linear in the size of the string, and we count every string.

Space Complexity: O(N * K), the total information content stored in result dict.
'''


def groupAnagrams(strs):
	"""
    :type strs: List[str]
    :rtype: List[List[str]]
    """
	if not strs:
		return []

	result = {}

	for s in strs:
		char_count = [0] * 26
		for ch in s:
			index = ord(ch) - ord('a')
			char_count[index] += 1

		# tuple can be dict key. List cannot be a dict key.
		key = tuple(char_count)
		if key in result:
			result[key].append(s)
		else:
			result[key] = [s]

	return result.values()




'''
Solution 2:
Sort every word and use it as key in dict. For each key, the value is an array of the corresponding strings
that are all anagrams

Complexity Analysis

Time Complexity: O(NK log (K)), where N is the length of strs, and K is the maximum length of a string in strs. 
The outer loop has complexity O(N) as we iterate through each string. Then, we sort each string in O(K log K) time.

Space Complexity: O(N*K), the total information content stored in the result dict.
'''


def groupAnagrams(strs):
	"""
    :type strs: List[str]
    :rtype: List[List[str]]
    """
	if not strs:
		return []

	result = {}

	for s in strs:
		sorted_word = ''.join(sorted(s))
		if sorted_word in result:
			result[sorted_word].append(s)
		else:
			result[sorted_word] = [s]

	return result.values()
