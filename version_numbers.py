#!/usr/bin/env python
'''
Compare two version numbers version1 and version2.
If version1 > version2 return 1, if version1 < version2 return -1, otherwise return 0.

You may assume that the version strings are non-empty and contain only digits and the . character.
The . character does not represent a decimal point and is used to separate number sequences.
For instance, 2.5 is not "two and a half" or "half way to version three", it is the fifth second-level revision of the second first-level revision.

Here is an example of version numbers ordering:

0.1 < 1.1 < 1.2 < 13.37
'''

def compareVersion(version1, version2):

    # both empty
    if not (version1 or version2):
        return 0
        
    version1 = version1.split('.')
    version2 = version2.split('.')

    m, n = 0, 0

    res = 0

    while m < len(version1) and n < len(version2):

        # incorrect answer if not converted to int
        num1 = int(version1[m])
        num2 = int(version2[n])

        if num1 > num2:
            return 1

        elif num1 < num2:
            return -1

        else:
            m += 1
            n += 1


    if m < len(version1) and n == len(version2):
        if int(version1[m]) != 0:
            res =  1
       

    if m == len(version1) and n < len(version2):
        if int(version2[n]) != 0:
            res = -1


    if m == len(version1) and n == len(version2):
        if int(version1[m - 1]) == int(version2[n -1]):
            res =  0

        elif int(version1[m -1]) > int(version2[n - 1]):
            res =  1

        else:
            res = -1

    return res
    
if __name__ == '__main__':
    print compareVersion('1.0', '1')
    

    

    
