#!/usr/bin/env python
'''
Given a string containing only digits, restore it by returning all possible valid IP address combinations.

For example:
Given "25525511135",

return ["255.255.11.135", "255.255.111.35"]. (Order does not matter)


Solution:
1) 3-loop divides the string s into 4 substring: s1, s2, s3, s4. 

2) Check if each substring is valid. 
In isValid, strings whose length greater than 3 or equals to 0 is not valid; 
or if the string's length is longer than 1 and the first letter is '0' then it's invalid; 
or the string whose integer representation greater than 255 is invalid.

'''
def restoreIpAddresses(s):

    if not s:
	return []


    result = []  

    for i in range(1, 4):
	    if len(s) - i > 9:        # if str has length of 12, 1st octet must have size 3, This condition not necessary for accuracy 
	        continue

	    for j in range(i + 1, i + 4):
	        if len(s) - j > 6:      # This condition not necessary for accuracy
		        continue

	        for k in range(j + 1, j + 4):
		        s1 = s[:i]
		        s2 = s[i : j]
		        s3 = s[j: k]
		        s4 = s[k:]
	      

		        if isValid(s1) and isValid(s2) and isValid(s3) and isValid(s4):
		            result.append(s1 + '.' + s2 + '.' + s3 + '.' + s4)

    return result


def isValid(s):
    if not s or len(s) > 3 or (s[0] == '0' and len(s) > 1) or int(s) > 255:
        return False

    return True
