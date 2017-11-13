#!/usr/bin/env python
"""
Follow up for H-Index: What if the citations array is sorted in ascending order? Could you optimize your algorithm?

Solution: Binary Search
"""


def hIndex(citations):
    """
    :type citations: List[int]
    :rtype: int
    """
    if not citations:
        return 0

    low = 0
    high = len(citations) - 1

    while low <= high:
        mid = low + (high - low) / 2

        if citations[mid] == len(citations) - mid:
            return citations[mid]

        elif citations[mid] < len(citations) - mid:
            low = mid + 1

        else:
            high = mid - 1

    return len(citations) - low
