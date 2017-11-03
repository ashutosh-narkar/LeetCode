#!/usr/bin/env python
'''
In a party of N people, only one person is known to everyone.
Such a person may be present in the party, if yes, (s)he doesn't know anyone in the party.
We can only ask questions like "does A know B? ".
Find the stranger (celebrity) in minimum number of questions.

Solution:
The first loop is to exclude n - 1 labels that are not possible to be a celebrity.
After the first loop, x is the only candidate.

The second and third loop is to verify x is actually a celebrity by definition.

The key part is the first loop. To understand this you can think the knows(a,b) as a a < b comparison,
if a knows b then a < b, if a does not know b, a > b.
Then if there is a celebrity, he/she must be the "maximum" of the n people.

However, the "maximum" may not be the celebrity in the case of no celebrity at all.
Thus we need the second and third loop to check if x is actually celebrity by definition.

The total calls of knows is thus 3n at most. One small improvement is that in the second loop
we only need to check i in the range [0, x). You can figure that out yourself easily.
'''


def find_celebrity(n):
    x = 0
    for i in range(n):
        if knows(x, i):
            x = i

    # check if the possible celebrity knows no one
    for i in range(n):
        if knows(x, i):
            return -1

    # check if everybody knows the celebrity
    for i in range(n):
        if not knows(i, x):
            return -1

    return x

