#!/usr/bin/env python
'''
Given an array of words and a length L, format the text such that each line has exactly L characters
and is fully (left and right) justified.

You should pack your words in a greedy approach; that is, pack as many words as you can in each line.
Pad extra spaces ' ' when necessary so that each line has exactly L characters.

Extra spaces between words should be distributed as evenly as possible.
If the number of spaces on a line do not divide evenly between words,
the empty slots on the left will be assigned more spaces than the slots on the right.

For the last line of text, it should be left justified and no extra space is inserted between words.

For example,
words: ["This", "is", "an", "example", "of", "text", "justification."]
L: 16.

Return the formatted lines as:
[
   "This    is    an",
   "example  of text",
   "justification.  "
]
Note: Each word is guaranteed not to exceed L in length.

'''

# @param L, an integer
# @return a list of strings


# TODO READ http://xxyxyz.org/line-breaking/
# http://www.geeksforgeeks.org/dynamic-programming-set-18-word-wrap/
def fullJustify_dp(words, width):
    count = len(words)
    slack = [[0] * count for i in range(count)]
    for i in range(count):
        slack[i][i] = width - len(words[i])
        for j in range(i + 1, count):
            slack[i][j] = slack[i][j - 1] - len(words[j]) - 1

    minima = [0] + [10 ** 20] * count
    breaks = [0] * count
    for j in range(count):
        i = j
        while i >= 0:
            if slack[i][j] < 0:
                cost = 10 ** 10
            else:
                cost = minima[i] + slack[i][j] ** 2
            if minima[j + 1] > cost:
                minima[j + 1] = cost
                breaks[j] = i
            i -= 1

    lines = []
    j = count
    while j > 0:
        i = breaks[j - 1]
        lines.append(' '.join(words[i:j]))
        j = i
    lines.reverse()
    return lines


def fullJustify(words, L):

    if not words:
        return []

    i = 0

    result = []
    temp = []

    while i < len(words):
        temp.append(words[i])
        total_len = sum(map(len, temp))

        if total_len < L:
            temp.append(' ')
            i += 1


        elif total_len == L:
            temp = ''.join(temp)
            result.append(temp)
            temp = []
            i += 1

            
        elif total_len > L:
            temp.pop()
            spaces = L - sum(map(len, temp))
            temp.append(' ' * spaces)
            temp = ''.join(temp)
            result.append(temp)
            temp = []

    if temp:
        result.append(''.join(temp))

    if len(result[-1]) == L:
        return result

    spaces = L - len(result[-1])
    last_line = result.pop() + ' '*spaces
    result.append(last_line)

    return result


if __name__ == '__main__':
    result = fullJustify(["Listen","to","many,","speak","to","a","few."], 6)
    for item in result:
        print item



    print '\n DP solution'
    result = fullJustify_dp(["Listen","to","many,","speak","to","a","few."], 6)
    for item in result:
        print item









