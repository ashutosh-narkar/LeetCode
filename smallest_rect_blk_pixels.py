#!/usr/bin/env python
"""
An image is represented by a binary matrix with 0 as a white pixel and 1 as a black pixel.
The black pixels are connected, i.e., there is only one black region.
Pixels are connected horizontally and vertically. Given the location (x, y) of one of the black pixels,
return the area of the smallest (axis-aligned) rectangle that encloses all black pixels.

For example, given the following image:
[
  "0010",
  "0110",
  "0100"
]
and x = 0, y = 2,
Return 6.

Solution:
We find the 4 boundaries given a black pixel in the following manner:
1) Use a vertical line, to jump to the leftmost black pixel , in the range of [0, y]
2) Use a vertical line, to jump to the rightmost black pixel, in the range of [y, n - 1]
3) Use a horizontal line, to jump to the topmost black pixel, in the range of [0, x]
4) Use a horizontal line, to jump to the bottommost black pixel, in the range of [x, m - 1]

This means we can do a binary search in each half to find the boundaries,
if we know one black pixel's position. And we do know that.

To find the left boundary, do the binary search in the [0, y) range and
find the first column vector who has any black pixel.

To determine if a column vector has a black pixel is O(m) so the search in total is O(m log n)

We can do the same for the other boundaries. The area is then calculated by the boundaries.
Thus the algorithm runs in O(m log n + n log m)
"""


def min_area(image, x, y):
    if not image:
        return 0

    nrows = len(image)
    ncols = len(image[0])

    top = search_row(image, 0, x, True)
    bottom = search_row(image, x + 1, nrows, False)

    left = search_col(image, 0, y, top, bottom, True)
    right = search_col(image, y + 1, ncols, top, bottom, False)

    return (right - left) * (bottom - top)


# go_up indicates whether we should move upwards after finding a black pixel
# search_row searches for a row vector with a black pixel (ie. 1)
def search_row(image, min_row, max_row, go_up):
    while min_row < max_row:
        mid = min_row + (max_row - min_row) / 2

        if '1' in image[mid] == go_up:
            max_row = mid

        else:
            min_row = mid + 1

    return min_row


# search_col searches for a column vector with a black pixel (ie. 1)
def search_col(image, min_col, max_col, min_row, max_row, go_up):
    while min_col < max_col:
        mid = min_col + (max_col - min_col) / 2

        if any(image[row][mid] == '1' for row in range(min_row, max_row)) == go_up:
            max_col = mid
        else:
            min_col = mid + 1

    return min_col

if __name__ == '__main__':
    image = ["0010", "0110", "0100"]
    x, y = 0, 2

    print min_area(image,x, y)
