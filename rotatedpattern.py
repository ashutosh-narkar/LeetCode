#!/usr/bin/env python

'''
Find whether a string is a rotation of another string
eg 'waterbottle' is a rotation of 'erbotthewat'.

Idea: s2 will always be a substring of s1s1
'''

def is_rotation(s1, s2):
    '''
    Check if s1 is a rotation of s2
    '''
    if len(s1) != len(s2):
        return False

    return s1 in s2 + s2


if __name__ == '__main__':
    res = is_rotation('waterbottle', 'erbottlewat')
    if res:
        print 'Yes they are rotations'
    else:
        print 'Not rotations'    
