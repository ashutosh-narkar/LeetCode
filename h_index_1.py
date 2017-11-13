#!/usr/bin/env python
"""
Given an array of citations (each citation is a non-negative integer) of a researcher,
write a function to compute the researcher's h-index.

According to the definition of h-index on Wikipedia:
"A scientist has index h if h of his/her N papers have at least h citations each, and the other N - h
papers have no more than h citations each."

For example, given citations = [3, 0, 6, 1, 5], which means the researcher has 5 papers in total
and each of them had received 3, 0, 6, 1, 5 citations respectively.
Since the researcher has 3 papers with at least 3 citations each and the remaining
two with no more than 3 citations each, his h-index is 3.

Note: If there are several possible values for h, the maximum one is taken as the h-index.

Solution:
1) Assume n is the total number of papers, then we have n+1 buckets, number from 0 to n
2) For any paper with reference corresponding to the index of the bucket, we increment the count for that bucket.
The only exception is that for any paper with larger number of reference than n, we put in the n-th bucket.
3) Then we iterate from the back to the front of the buckets, whenever the total count exceeds the index of the bucket,
meaning that we have the index number of papers that have reference greater than or equal to the index.
Which will be our h-index result.

The reason to scan from the end of the array is that we are looking for the greatest h-index
"""


def hIndex(citations):
    """
    :type citations: List[int]
    :rtype: int
    """
    if not citations:
        return 0

    n = len(citations)
    buckets = [0] * (n + 1)

    for citation in citations:
        if citation >= n:
            buckets[n] += 1
        else:
            buckets[citation] += 1

    count = 0
    for i in range(len(buckets) - 1, - 1, -1):
        count += buckets[i]
        if count >= i:
            return i

    return 0
