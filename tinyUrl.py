#!/usr/bin/env python
"""
TinyURL is a URL shortening service where you enter a URL such as
https://leetcode.com/problems/design-tinyurl and it returns a short URL such as http://tinyurl.com/4e9iAk.

Design the encode and decode methods for the TinyURL service.
There is no restriction on how your encode/decode algorithm should work.
You just need to ensure that a URL can be encoded to a tiny URL and the tiny URL can be decoded to the original URL.


Analysis:
If the code length is 7 containing [A-Z, a-z, 0-9], we can serve 62 ^ 7 ~= 3500 billion URLs.


More analysis: http://blog.gainlo.co/index.php/2016/03/08/system-design-interview-question-create-tinyurl-system/
"""

import string
import random


class Codec:
    def __init__(self):
        self.url_to_code = {}
        self.code_to_url = {}

        self.codeLength = 6
        self.alphabet = string.ascii_letters + '0123456789'
        self.base_url = 'http://tinyurl.com/'

    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.

        :type longUrl: str
        :rtype: str
        """
        if longUrl in self.url_to_code:
            code = self.url_to_code[longUrl]
            return self.base_url + code

        else:
            while longUrl not in self.url_to_code:
                code = ''.join([random.choice(self.alphabet) for _ in range(self.codeLength)])
                if code not in self.code_to_url:
                    self.code_to_url[code] = longUrl
                    self.url_to_code[longUrl] = code

            return self.base_url + self.url_to_code[longUrl]

    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.

        :type shortUrl: str
        :rtype: str
        """
        code = shortUrl[-6:]
        if code not in self.code_to_url:
            return ""

        return self.code_to_url[code]


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))