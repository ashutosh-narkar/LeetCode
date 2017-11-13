#!/usr/bin/env python
"""
Design an algorithm to encode a list of strings to a string.
The encoded string is then sent over the network and is decoded back to the original list of strings.

Note:
1) The string may contain any possible characters out of 256 valid ascii characters.
Your algorithm should be generalized enough to work on any possible characters.

2) Do not use class member/global/static variables to store states.
Your encode and decode algorithms should be stateless.

3) Do not rely on any library method such as eval or serialize methods.
You should implement your own encode/decode algorithm.
"""
import string

def encode(str_list):

    if not str_list:
        return ""

    result = ''
    for item in str_list:
        temp = str(len(item)) + '/' + item    # len_of_str + '/' + str
        result += temp

    return result


def decode(s):
    if not s:
        return []

    result = []
    i = 0

    while i < len(s):
        slash = string.index(s, '/', i)
        size = int(s[i: slash])
        result.append(s[slash + 1: slash + 1 + size])
        i = slash + size + 1

    return result

if __name__ == '__main__':
    encoded_str = encode(['a', 'b', 'c'])
    assert decode(encoded_str) == ['a', 'b', 'c']

    encoded_str = encode(['a', '5', 'b', 'c', '4'])
    decode(encoded_str) == ['a', '5', 'b', 'c', '4']

    encoded_str = encode(['a', '5', '', 'c', '4'])
    decode(encoded_str) == ['a', '5', '', 'c', '4']

    print 'Tests passed'
