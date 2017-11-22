#!/usr/bin/env python
'''
Given a string, find the length of the longest substring without repeating characters.
For example, the longest substring without repeating letters for "abcabcbb" is "abc", 
which the length is 3. For "bbbbb" the longest substring is "b", with the length of 1.


This problem can also be solved using Kadane's algo. But Solution1 is comparable
in terms of time and space complexity
'''


import sys 

# Solution 1: Runtime O(n). Space O(256 Ascii chars)
# Step 1: Maintain a dict of char and its index
# Step 2: Have 2 pointers 'low' and 'high' to mark start and end of the substring respectively
# Step 3: Update the low pointer if a duplicate character found


def longest_substring_1(s):
    """
    :type s: str
    :rtype: int
    """

    if not s:
        return 0

    charIndex = {}

    low, high = 0, 0
    max_length = 0
    result = ""

    while high < len(s):
        if s[high] in charIndex:
            low = max(low, charIndex[s[high]] + 1)    # We dont do low = charCount[s[high]] + 1 as low may
                                                      # point to a index that was already removed from the dict.
                                                      # eg. 'abba'

        charIndex[s[high]] = high

        # update result
        curr_len = high - low + 1
        if max_length < curr_len:
            max_length = curr_len
            result = s[low: high + 1]

        high += 1

    return result


# Solution 2: Don't use

def longest_substring_2(data):
    if not data:
        return

    max_string = ''
    current_max = ''

    for i in range(len(data)):
        if data[i] in current_max:
            max_string = max_string if len(max_string) > len(current_max) else current_max

            # go back in the string, till we find data[i]
            # and return index of char after that
            index = getIndex(data, i)
            current_max = data[index: i+1]

        else:
            current_max += data[i]


    # entire string contains non-repeated characters
    # or last few characters comprise the longest substring eg. abcdaaabcdeecdaghjil
    max_string = max_string if len(max_string) > len(current_max) else current_max
    return max_string

def getIndex(s, index):
    char = s[index]

    i = index  - 1
    while i >= 0:
        if s[i] == char:
            return i + 1
        i -= 1


if __name__ == '__main__':
    res = longest_substring_1(sys.argv[1])
    print 'Longest substring w/o repeated chars: "{}" len: {}'.format(res, len(res))

    res = longest_substring_2(sys.argv[1])
    print 'Longest substring w/o repeated chars: "{}" len: {}'.format(res, len(res))

