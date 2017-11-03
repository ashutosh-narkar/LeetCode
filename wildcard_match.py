#!/usr/bin/env python
'''
mplement wildcard pattern matching with support for '?' and '*'.

'?' Matches any single character.
'*' Matches any sequence of characters (including the empty sequence).

The matching should cover the entire input string (not partial).

The function prototype should be:
bool isMatch(const char *s, const char *p)

Some examples:
isMatch("aa","a") → false
isMatch("aa","aa") → true
isMatch("aaa","aa") → false
isMatch("aa", "*") → true
isMatch("aa", "a*") → true
isMatch("ab", "?*") → true
isMatch("aab", "c*a*b") → false



Solution:

For each element in s

Case 1: If *s==*p or *p == ? which means this is a match, then goes to next element s++ p++.

Case 2: If p=='*', this is also a match, but one or many chars may be available, so let us save this *'s position and the matched s position.

Case 3: if not match, then we check if there is a * previously showed up,
           3.1) if there is no *,  return false;
           3.2) if there is an *,  we set current p to the next element of *, and set current s to the next saved s position.

Runtime:  complexity of the algorithm is O(p*s), where p and s are the lengths of the pattern and input strings.
'''

def isMatch(s, p):


    s_index = 0
    p_index = 0


    match = -1
    star = -1


    while s_index < len(s):
        # case 1
	    if p_index < len(p) and  (s[s_index] == p[p_index] or p[p_index] == '?'):
	        s_index += 1
	        p_index += 1

	    
        # case 2
	    elif p_index < len(p) and p[p_index] == '*':
	        match = s_index
	        star = p_index
	        p_index += 1

	    # case 3.2    
	    elif star != -1:
	        p_index = star + 1
	        match += 1
	        s_index = match
	    
        # case 3.1
    	else:
	        return False


	
    # check the rest element in p, if all are *, true, else false;
    while p_index < len(p) and p[p_index]  == '*':
	    p_index += 1


    if len(p) == p_index:

	    return True

    return False



############ Solution 2 ################
def isMatch_dp(s, p):


    if len(p) - p.count('*') > len(s):
	return False


   # initialize the matrix
    dp = [False] * (len(p) + 1)


    # empty string matches empty string
    dp[0] = True


    # if the string is empty,
    # current char of the pattern should be a '*' and depends on the previous result    
    for i in range(1, len(p) + 1):
	dp[i] = (p[i - 1] == '*') and dp[i - 1]



    for i in range(1, len(s) + 1):
	cur = [False] * (len(p) + 1)

	for j in range(1, len(p) + 1):
	    if p[j - 1] != '*':
		cur[j] = (p[j - 1] == s[i -1] or p[j - 1] == '?') and dp[j -1]

            # tricky case when current char pof pattern is not '*'
            # current cell value is true if its top or its left is true.
	    else:
		cur[j] = cur[j - 1] or dp[j]

	dp = cur

    

    return dp[-1]




























