#!/usr/bin/env python
'''
Implement strStr().

Returns the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Good Explanation: https://www.topcoder.com/community/data-science/data-science-tutorials/introduction-to-string-searching-algorithms/

OK-OK Explanation - http://www.geeksforgeeks.org/searching-for-patterns-set-2-kmp-algorithm/
'''

def strStr(self, haystack, needle):

    if not needle:
        return 0
     
    # create lps that will hold the longest prefix suffix values for pattern
    lps = computeLps(needle)
    i = 0
    j = 0

     
    while i < len(haystack):

        if haystack[i] == needle[j]:
            i += 1
            j += 1

         
        # pattern found
        if j == len(needle):
            return i-j

        # mismatch after j steps
        elif i < len(haystack) and haystack[i] != needle[j]:
 
            # move ahead in the string if we are at beginning of pattern. May be we find a match later
            if j == 0:
                i += 1

            # we do not need to match all characters since, we know pat[0 to j-1] matches txt[i-j to i-1]
            else:
                j = lps[j-1]

    return -1

        

def computeLps(needle):

    # L[0] = 0  always
    lps = [0] * len(needle)

    # length of the previous longest prefix suffix
    lon = 0

    i = 1

    while i < len(needle):
        if needle[lon] == needle[i]:
            lon += 1
            lps[i] = lon
            i += 1

        else:
            if lon == 0:
                lps[i] = 0
                i += 1

            else:
                # go to the next best "candidate" partial match
                lon = lps[lon-1]

    return lps



#####################################################################################################
'''
Solution 2: Brute Force . Runtime: 

The “naive” approach is easy to understand and implement but it can be too slow in some cases. 
If the length of the text is n and the length of the pattern m, in the worst case it may take as much as (n * m) iterations to complete the task.

It should be noted though, that for most practical purposes, which deal with texts based on human languages, 
this approach is much faster since the inner loop usually quickly finds a mismatch and breaks. 
A problem arises when we are faced with different kinds of “texts,” such as the genetic code.
'''

# @param haystack, a string
# @param needle, a string
# @return an integer
def strStr(haystack, needle):

    if not needle:
        return 0


    lh = len(haystack)
    ln = len(needle)

    if ln > lh:
        return -1
        

    # Iterate over 'lh-ln + 1' since it indicates the possible starting points
    # in the give text (or haystack) in which the pattern(or needle can be searched)
    # eg. text=ashutosh, pattern=ut, there are 7 possible position in the text where pattern can be searched from

    for i in range(lh - ln + 1):

        j = 0
        while haystack[i + j] == needle[j]:
            j += 1

            if j == ln:
                return i

    return -1




