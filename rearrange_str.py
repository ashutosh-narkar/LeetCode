#!/usr/bin/env python
'''
Given a non-empty string str and an integer k, rearrange the string such that the same
characters are at least distance k from each other.

All input strings are given in lowercase letters.
If it is not possible to rearrange the string, return an empty string "".

Example 1:
str = "aabbcc", k = 3

Result: "abcabc"

The same letters are at least distance 3 from each other.
Example 2:
str = "aaabc", k = 3

Answer: ""

It is not possible to rearrange the string.

Example 3:
str = "aaadbbcc", k = 2

Answer: "abacabcd"

Another possible answer is: "abcabcda"

The same letters are at least distance 2 from each other.


Solution:
The idea is simple: we only worry about the most frequent character(s).

For example aaaabbbbcccddefg, 'a' is the most frequent letter, so we start with a structure like
a [] a [] a [] a []

and we just pad other letters in between the a's.
Only letters with the same highest frequency can go in to the last [].
and we don't care about any letters with lower frequencies, we just scatter them among the paddings.

So we end up with
a [bcdf] a [bcdg] a [bce] a [b].

If all the paddings except the last one have length larger than k-1, then we have our answer; else we return ''.

Similar question: task_scheduler.py
'''


def rearrangeString(string, k):
    if not string:
        return ''

    count = {}
    for s in string:
        if s in count:
            count[s] += 1
        else:
            count[s] = 1

    # sort the letters according to the frequency
    stack = sorted(count.items(), key=lambda x: x[1])

    char, count = stack.pop()  # get most frequent character

    # create the padding structures
    lst = [[char] for _ in range(count)]

    # take care of the letters with same highest freq
    while stack and stack[-1][1] == count:
        char, _ = stack.pop()
        for l in lst:
            l.append(char)

    # all the characters left
    res = ''.join(c * n for c, n in stack)


    # padding
    for i, r in enumerate(res):
        lst[i % (len(lst) - 1)].append(r)

    # If all the paddings except the last one have length larger than k-1, then we have our answer; else we return ''.
    # Since if the padding length is less than k, the our least distance condition is violated
    for l in lst[:-1]:
        if len(l) < k:
            return ''

    return ''.join(''.join(l) for l in lst)

if __name__ == '__main__':
    print rearrangeString("aaabc", 3)