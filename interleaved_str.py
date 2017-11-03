#!/usr/bin/env python
'''
Given s1, s2, s3, find whether s3 is formed by the interleaving of s1 and s2.

For example,
Given:
s1 = 'aabcc'
s2 = 'dbbca'

When s3 = 'aadbbcbcac', return true.
When s3 = 'aadbbbaccc', return false.

M = len(s1), N = len(s2)
Time Complexity: O(MN)
Auxiliary Space: O(MN)
'''

def isInterleave(s1, s2, s3):

    m = len(s1)
    n = len(s2)

    # s3 can be an interleaving of s1 and s2 only if sum
    # of lengths of s1 & s2 is equal to length of s3.
    if m + n != len(s3):
        return False

    res = []
    
    # Initialize all values as false
    row = [False] * (n + 1)
    for i in range(m + 1):
        res.insert(i, row)


    for i in range(m + 1):
        for j in range(n + 1):

            # two empty string have an empty
            # string as an interleaving
            if i == 0 and j == 0:
                res[i][i] = True

            # s1 is empty
            elif i == 0 and s2 and s2[j - 1] == s3[ i + j - 1]:   # We need to check if s1 and/or s2 exits to prevent indexing an empty string
                res[i][j] = res[i][j - 1]

            # s2 is empty
            elif j == 0 and s1 and s1[i - 1] == s3[i + j - 1]:
                res[i][j] == res[i - 1][j]


            # Current character of s3 matches with current character of s1,
            # but doesn't match with current character of s2
            elif s1 and s1[i - 1] == s3[i + j - 1] and s2 and s2[j - 1] != s3[i + j - 1]:
                res[i][j] = res[i - 1][j] 


            # Current character of s3 matches with current character of s2,
            # but doesn't match with current character of s1
            elif s1 and s1[i - 1] != s3[i + j - 1] and s2 and s2[j - 1] == s3[i + j - 1]:
                res[i][j] = res[i][j - 1]

            # Current character of s3 matches with current character of s1 and s2
            elif s1 and s1[i - 1] == s3[i + j - 1] and s2 and s2[j - 1] == s3[i + j - 1]:
                res[i][j] = res[i - 1][j] or res[i][j - 1] 

            # Current character of s3 matches with neither s1 or s2 current character
            else:
                res[i][j] = False


    return res[m][n]



if __name__ == '__main__':

    assert isInterleave("XXY", "XXZ", "XXZXXXY") == False
    assert isInterleave("XY" ,"WZ" ,"WZXY") == True
    assert isInterleave("XY", "X", "XXY") == True
    assert isInterleave("XXY", "XXZ", "XXXXZY") == True
    assert isInterleave("abcd", "xyz", "axybczd") == True
    assert isInterleave("AB", "CD", "CADB") == True
    assert isInterleave("AB" ,"CD" ,"CDAB") == True
    assert isInterleave("AB" , "A" , "AAB") == True
    assert isInterleave("A" ,"AB" ,"ABA") == True
    assert isInterleave("A" ,"AB", "BAA") == False
    assert isInterleave("ACA" ,"DAS" ,"DAACSA") == True
    assert isInterleave("ACA" ,"DAS" ,"DAASCA") == True
    assert isInterleave("A", "AB" ,"AAB") == True
    assert isInterleave("AAB" ,"AAC" ,"AACAAB") == True
    assert isInterleave("101", "01", "10011") == True
    assert isInterleave("101" ,"01" ,"11010") == False
    assert isInterleave("A" ,"C", "CA") == True
    assert isInterleave("A", "C", "CD") == False
    assert isInterleave("ACA" ,"DAS", "ADASAC") == False
    assert  isInterleave("YX", "X", "XXY") == False

    print 'Tests  passed'










