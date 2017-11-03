#!/usr/bin/env python
'''
Given a non-negative number represented as an array of digits, plus one to the number.

The digits are stored such that the most significant digit is at the head of the list.

Just consider two special cases:
(1) last digit is 9: need a carry
(2) All the digits are 9 just return 100000... number of 0s is the length of the vector.

'''


def plus_one(self, digits):
	"""
	:type digits: List[int]
    :rtype: List[int]
    """

	if digits[-1] != 9:
		digits[-1] += 1
		return digits

	else:
		digits[-1] = 0
		for i in range(len(digits) - 2, - 1, -1):
			if digits[i] != 9:
				digits[i] += 1
				return digits

			else:
				digits[i] = 0

		# all 9's
		digits.insert(0, 1)
		return digits
