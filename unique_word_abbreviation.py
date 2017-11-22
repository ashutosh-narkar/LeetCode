#!/usr/bin/env python
"""
An abbreviation of a word follows the form <first letter><number><last letter>.

Below are some examples of word abbreviations:
a) it                      --> it    (no abbreviation)

     1
b) d|o|g                   --> d1g

              1    1  1
     1---5----0----5--8
c) i|nternationalizatio|n  --> i18n

              1
     1---5----0
d) l|ocalizatio|n          --> l10n


Assume you have a dictionary and given a word, find whether its abbreviation is unique in the dictionary.
A word's abbreviation is unique if no other word from the dictionary has the same abbreviation.

Given dictionary = [ "deer", "door", "cake", "card" ]

isUnique("dear") -> false
isUnique("cart") -> true
isUnique("cane") -> false
isUnique("make") -> true


Given dictionary = ["a","a"]

isUnique("a") -> true
"""


class ValidWordAbbr:
    def __init__(self, dictionary):
        self.abbrev_word = dict()    # abbreviation -> word

        for word in dictionary:
            key = self.get_key(word)

            # If there is more than one string belonging to the same key
            # then the key will be invalid, we set the value to ""
            if key in self.abbrev_word:
                if self.abbrev_word[key] != word:
                    self.abbrev_word[key] = ""

            else:
                self.abbrev_word[key] = word

    # There are only 2 conditions we return true for isUnique("word")
    # 1. The abbr does not appear in the dict.
    # 2. The abbr is in the dict && the word appears one and only once in the dict.
    def is_unique(self, word):
        key = self.get_key(word)

        # The abbr does not appear in the dict
        if key not in self.abbrev_word:
            return True

        # The abbr is in the dict && the word appears one and only once in the dict
        if self.abbrev_word[key] == word:
            return True

        return False

    def get_key(self, s):
        if len(s) <= 2:
            return s

        # <first letter><number><last letter>
        return s[0] + str(len(s) - 2) + s[-1]

if __name__ == '__main__':
    vwa = ValidWordAbbr(["deer", "door", "cake", "card" ])
    assert vwa.is_unique('dear') == False
    assert vwa.is_unique('cart') == True
    assert vwa.is_unique('cane') == False
    assert vwa.is_unique('make') == True

    vwa = ValidWordAbbr(['a', 'a'])
    assert vwa.is_unique('a') == True

    print "Tests Passed"
