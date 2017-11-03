#!/usr/bin/env python
'''
Implement regular expression matching with support for '.' and '*'.
'.' Matches any single character.
'*' Matches zero or more of the preceding element.

The matching should cover the entire input string (not partial).

The function prototype should be:
bool isMatch(const char *s, const char *p)

Some examples:
isMatch("aa","a") is false
isMatch("aa","aa") is true
isMatch("aaa","aa") is false
isMatch("aa", "a*") is true
isMatch("aa", ".*") is true
isMatch("ab", ".*") is true
isMatch("aab", "c*a*b") is true
'''

def isMatch(s, p):

    if not p:
	    return len(s) == 0
    
    if len(p) == 1 or p[1] != '*':

        # first char of string and pattern don't match and
        # pattern char is not '.'. But since pattern size is
        # atleast as big as string, there is a chance of future match
        if (s and s[0] != p[0] and p[0] != '.' and len(s) <= len(p)):
            return isMatch(s, p[1:])

	if len(s) < 1 or (s[0] != p[0] and p[0] != '.'):
	    return False
	return isMatch(s[1:], p[1:])


    else:
        # need to start i from -1 for case where
        # s is empty and next char of p is '*'
        # eg s = 'a' p = 'ab*'
	i = -1
	while i < len(s) and (i < 0 or s[i] == p[0] or p[0] == '.'):
	    if isMatch(s[i + 1:], p[2:]):
		return True

	    i += 1

	return False



def isMatch_dp(s, p):

    # initialize the matrix
    dp = [[False] * (len(s) + 1) for i in range(len(p) + 1)]

    # empty string matches empty string
    dp[0][0] = True

    
    # if the string is empty,
    # current char of the pattern should be a '*' and depends on the previous result    
    for i in range(1, len(p)):
	dp[i + 1][0] = p[i] == '*' and dp[i - 1][0]


    for i in range(len(p)):
	for j in range(len(s)):

            # if current patter character not a '*'
            # then current pattern char should match the current string OR current pattern char should be a '.'
            # AND depends on previous result 
	    if p[i] != '*':
		dp[i + 1][j + 1] = (p[i] == s[j] or p[i] == '.') and dp[i][j] 

        
            # if the current pattern character is a  '*' there are 3 cases:
            # 1) previous char of pattern repeated 0 times: this means we need to match previous of previous pattern character with current string char ie. dp[i - 1][j + 1]
            # 2) previous char of pattern repeated 1 time: this means we need to match previous pattern character with current string char ie. dp[i][j + 1]
            # 3) previous char of pattern repeated 2 or more times: this means we need to match current character of pattern with current character of string AND
            # 
	
 
	    else:
                #                     case 2             case1
		dp[i + 1][j + 1] = dp[i][j + 1] or dp[i - 1][j + 1]
		
                # case 3
                if p[i - 1] == s[j] or p[i - 1] == '.':
		    dp[i + 1][j + 1] |= dp[i + 1][j]             # confusing


    return dp[-1][-1]



def isMatch(s, p):


    m = len(s)
    n = len(p)

    dp = [[False] * (n + 1) for i in range(m + 1)]

    
    # empty string matches empty string
    dp[0][0] =  True


    # if the string is empty,
    # '*' should not  be the first character of pattern
    # '*' can be the 2nd, 4th, 6th char of the pattern. ie. index 1,3,5..
    for i in range(2, n + 1, 2):
        # result depends on the previous to previous character which should also be a '*'
        if p[i - 1] == '*' and dp[0][i - 2]:
            dp[0][i] = True

        # once we find a 'False' , everything after this would be false
        else:
            break


    for i in range(1, m + 1):
        for j in  range(1, n + 1):

            # if current patter character not a '*'
            # then current pattern char should match the current string OR current pattern char should be a '.'
            # AND depends on previous result 
            if p[j - 1] != '*':
                dp[i][j] = (s[i - 1] == p[j - 1] or p[j - 1] == '.') and dp[i - 1][j - 1]

    
            # if the current pattern character is a  '*' there are 3 cases:
            # 1) previous char of pattern repeated 0 times: this means we need to match previous of previous pattern character with current string char ie. dp[i][j - 2]
            # 2) previous char of pattern repeated 1 or more times then current char of string should match previous char of pattern (since current pattern char is '*')
            # or previous pattern char should be '.'. Now we also use the result prev string char with the current pattern char ie. dp[i -1][j]. This is because ...i dont know yet 
            else:
                dp[i][j] = dp[i][j - 2] or dp[i - 1][j] and (s[i - 1] == p[j - 2] or p[j - 2] == '.')

                

    return dp[-1][-1]




        
# ************** Optimal Solution *******************        
def isMatch(self, s, p):


    dp = [False] * (len(p) + 1)


    # empty string matches empty string
    dp[0] = True


    # if the string is empty,
    # '*' cannot be the first character of pattern
    # '*' can be the 2nd, 4th, 6th char of the pattern. ie. index 1,3,5..
    # eg. for string like "a*b*c*", make last/cur[indexOf('*')]=true.

    valid = False
    for i in range(2, len(p) + 1, 2):
	    if p[i - 1] == '*':
            valid = True
            d[i] = d[i - 2]   # result upto previous '*'. OR d[i] = True
        else:
            valid = False
 


    for i in range(1, len(s) + 1):
	    cur = [False] * (len(p) + 1)

	    for j in range(1, len(p) + 1):

            # case1: current char of the pattern is not '*' 
	        if p[j - 1] != '*':
		        cur[j] = (p[j - 1] == s[i - 1] or p[j - 1] == '.') and dp[j - 1]

            # case2: current char of the pattern is '*'
	        else:

                # case2.1 - current pattern char is '*' and prev pattern char matches curr char of string
                # This means we include everything upto current pattern and current string = dp[j]

                # case2.2 - current pattern char is '*' and prev pattern char is '.'
                # This means we are done. So take consider our result before the '.' = cur[j  -2]
                
		        if p[j - 2] == s[i - 1] or p[j - 2] == '.':
		            cur[j] = dp[j] or cur[j -2]

                # this means we have a mismatch. So use the result before the dot = cur[j -2]
		        else:
		            cur[j] = cur[j-2]


	    dp = cur

    return dp[-1]
    
if __name__ == '__main__':
    print isMatch_dp_2("aab", "c*a*b*")
