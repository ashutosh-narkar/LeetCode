#!/usr/bin/env python
"""
Freedom Trail

Question: https://leetcode.com/problems/freedom-trail/description/

Given a string ring, which represents the code engraved on the outer ring and another string key,
which represents the keyword needs to be spelled. You need to find the minimum number of steps in order
to spell all the characters in the keyword.

Initially, the first character of the ring is aligned at 12:00 direction. You need to spell all the characters
in the string key one by one by rotating the ring clockwise or anticlockwise to make each character of the string key
aligned at 12:00 direction and then by pressing the center button.

At the stage of rotating the ring to spell the key character key[i]:

1) You can rotate the ring clockwise or anticlockwise one place, which counts as 1 step.
The final purpose of the rotation is to align one of the string ring's characters at the 12:00 direction,
where this character must equal to the character key[i].


2) If the character key[i] has been aligned at the 12:00 direction, you need to press the center button to spell,
which also counts as 1 step. After the pressing, you could begin to spell the next character in the key (next stage),
otherwise, you've finished all the spelling.

"""


def find_rotate_steps(ring, key):
    """
    :type ring: str
    :type key: str
    :rtype: int
    """

    # {ch: list_of_indexes in the ring}
    char_index = {}
    for i, ch in enumerate(ring):
        if ch not in char_index:
            char_index[ch] = [i]

        else:
            char_index[ch].append(i)

    # the current possible state: {position of the ring: the cost}
    # For every character in the key, get the list of possible positions
    # Then from each start position calculate the min distance to each possible position

    current_state = {0: 0}
    for ch in key:
        next_positions = char_index[ch]
        next_state = {}

        for pos in next_positions:
            next_state[pos] = float('inf')
            for start_pos, cost in current_state.items():
                min_cost = dist(start_pos, pos, len(ring)) + cost
                next_state[pos] = min(next_state[pos], min_cost)

        current_state = next_state

    return min(current_state.values()) + len(key)


# the distance between two positions (i, j) can be defined as
def dist(i, j, ring_len):
    return min(abs(i - j), ring_len - abs(i - j))