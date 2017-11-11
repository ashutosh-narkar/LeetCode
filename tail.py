#!/usr/bin/env python
"""
Given some text lines in one string, each line is separated by '\n' character.
Print the last 'n' lines. If number of lines is less than 'n', then print all lines.
"""

import sys, argparse


def tail(path, lines_to_print):
    if lines_to_print < 1:
        return

    with open(path, 'r') as file:

        # 'seek' changes the file object's position. <f.seek(offset, from_what)>
        # Go to the last byte from the end
        # '2' uses the end of the file as the reference point. FYI '0' uses beginning and '1' uses current position
        # as reference point
        file.seek(-1,  2)

        # returns an integer giving the file object's current position in the file,
        # measured in bytes from the beginning of the file
        position = file.tell()
        lines_seen = 0

        # ignore the last instance of the delimiter '\n'
        if file.read(1) == '\n':
            position -= 1
            file.seek(position)

        while lines_seen < lines_to_print and file.tell() > 0:
            # reads 1 byte of data and returns it as a string
            c = file.read(1)
            if c == '\n':
                lines_seen += 1
                if lines_seen == lines_to_print:
                    break
            position -= 2           # Why decrement by 2 ?
            file.seek(position)
        sys.stdout.write(file.read())

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('path', help='The path to the file to tail')
    parser.add_argument('-n', help='Print the last n lines of the file', type=int, default=5)
    args = parser.parse_args()
    tail(args.path, args.n)