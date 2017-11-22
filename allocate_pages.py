#!/usr/bin/env python
"""
Given number of pages in n different books and m students.
The books are arranged in ascending order of number of pages.
Every student is assigned to read some consecutive books. The task is to assign books in such a way
that the maximum number of pages assigned to a student is minimum.

Input : pages[] = {12, 34, 67, 90}
        m = 2
Output : 113
Explanation:
There are 2 students. Books can be distributed
in following fashion :
  1) [12] and [34, 67, 90]
      Max number of pages is allocated to student
      2 with 34 + 67 + 90 = 191 pages
  2) [12, 34] and [67, 90]
      Max number of pages is allocated to student
      2 with 67 + 90 = 157 pages
  3) [12, 34, 67] and [90]
      Max number of pages is allocated to student
      1 with 12 + 34 + 67 = 113 pages

Of the 3 cases, Option 3 has the minimum pages = 113.

Solution:
The idea is to use Binary Search. We fix a value for number of pages as mid of current minimum and maximum.
We initialize minimum and maximum as 0 and sum-of-all-pages respectively.

If a current mid can be a solution, then we search on the lower half, else we search in higher half.

How to check if a mid value is feasible or not?
If we can allocate at most maximum x pages to each student and still satisfy at most M student.
"""


def find_pages(pages, m):

    n = len(pages)

    #  no. of books is less than
    # no. of students
    if n < m:
        return -1

    low = 0
    high = sum(pages)

    result = float('inf')

    while low <= high:
        mid = low + (high - low) / 2

        # check if it is possible to distribute
        # books by using mid is current minimum
        if is_possible(pages, mid, m):

            # if yes then find the minimum distribution
            result = min(result, mid)

            # as we are finding minimum and books
            # are sorted so reduce high = mid -1
            high = mid - 1

        else:
            # if not possible means pages should be
            # increased so update low = mid + 1
            low = mid + 1

    return result


def is_possible(pages, curr_min, num_students):
    count = 1   # count of students
    curr_sum = 0

    for page in pages:
        curr_sum += page

        # count how many students are required
        # to distribute curr_min pages
        if curr_sum > curr_min:
            count += 1
            curr_sum = page

    return count <= num_students

if __name__ == '__main__':
    pages = [12, 34, 67, 90]
    m = 2
    print find_pages(pages, m)
