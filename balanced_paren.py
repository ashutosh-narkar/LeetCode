#!/usr/bin/env python
'''
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

The brackets must close in the correct order,  "([])", ""()" and "()[]{}" are all valid but "(]" and "([)]" are not.
'''


def is_valid(s):

	if not s:
		return False

	if len(s) % 2 != 0:
		return False


	stack = []

	for ch in s:
		if ch in ('(', '[', '{'):
			stack.append(ch)

		else:
			if not stack:
				return False

			else:
				chr = stack.pop()

				if chr == '(' and ch != ')':
					return False
		    
				elif chr == '[' and ch != ']':
					return False
		    

				elif chr == '{' and ch != '}':
					return False

	if stack:
		return False

	return True

