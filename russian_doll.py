#!/usr/bin/env python
"""
You have a number of envelopes with widths and heights given as a pair of integers (w, h).
One envelope can fit into another if and only if both the width and height of one envelope
is greater than the width and height of the other envelope.

What is the maximum number of envelopes can you Russian doll? (put one inside other)

Example:
Given envelopes = [[5,4],[6,4],[6,7],[2,3]],
the maximum number of envelopes you can Russian doll is 3 ([2,3] => [5,4] => [6,7]).

Solution:

1) Sort the array. Ascend on width and descend on height if width are same.
2) Find the longest increasing subsequence based on height. Since the width is increasing,
we only need to consider height.

[3, 4] cannot contain [3, 3], so we need to put [3, 4] before [3, 3] when sorting otherwise
it will be counted as an increasing number if the order is [3, 3], [3, 4]
"""


def max_envelopes(envelopes):
    """
    :type envelopes: List[List[int]]
    :rtype: int
    """
    if not envelopes:
        return 0

    envelopes_sorted = sorted(envelopes, key=lambda x: (x[0], -x[1]))

    heights = [item[1] for item in envelopes_sorted]

    result = []

    for height in heights:
        if not result or result[-1] < height:
            result.append(height)

        else:
            low = 0
            high = len(result) - 1

            while low < high:
                mid = low + (high - low) / 2

                if result[mid] < height:
                    low = mid + 1

                else:
                    high = mid

            result[high] = height

    return len(result)

if __name__ == '__main__':
    envelopes = [[5, 4], [6, 4], [6, 7], [2, 3]]
    print max_envelopes(envelopes)
