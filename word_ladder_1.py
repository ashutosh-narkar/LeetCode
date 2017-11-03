#!/usr/bin/env python
'''
Given two words (start and end), and a dictionary, find the length of shortest transformation sequence from start to end, such that:

Only one letter can be changed at a time
Each intermediate word must exist in the dictionary
For example,

Given:
start = "hit"
end = "cog"
dict = ["hot","dot","dog","lot","log"]

As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog",
return its length 5.

Note:
Return 0 if there is no such transformation sequence.
All words have the same length.
All words contain only lowercase alphabetic characters.


Runtime:
The number of vertices is the number d of words in the dictionary. The number
of edges is, in the worst case, O(d2 ). The time complexity is that of BFS, namely
O(d + d2 ) = O(d2 ). (If the string length n is less than d then the number of edges drops
to O(n), implying an O(nd) bound.)

'''

from collections import deque


def ladderLength(beginWord, endWord, wordList):
	"""
	:type beginWord: str
    :type endWord: str
    :type wordList: List[str]
    :rtype: int
    """

	# pre-process the word list
	d = construct_dict(wordList)

	return bfs_words(beginWord, endWord, d)


def construct_dict(wordList):
	'''
    To find all words at edit distance 1, create a dict with key
    equal to word with '_' in all possible locations.
    eg 'pope' would result in keys '_ope', 'p_pe', 'po_e', 'pop_'

    Value would be list of words that match this pattern.
    eg .d['_ope'] = ['pope', 'rope', 'nope', 'hope']
    '''
	d = {}

	for word in wordList:
		for i in range(len(word)):
			pattern = word[:i] + '_' + word[i + 1:]
			if pattern in d:
				d[pattern].append(word)
			else:
				d[pattern] = [word]

	return d


def bfs_words(beginWord, endWord, dict_words):
	queue = deque()
	queue.append((beginWord, 1))  # initial length is 1
	visited = set()
	visited.add(beginWord)

	while queue:
		word, steps = queue.popleft()

		if word == endWord:
			return steps

		# find the connecting word to the current word
		for i in range(len(word)):
			pattern = word[:i] + '_' + word[i + 1:]
			neigh_words = dict_words.get(pattern, [])

			for neigh in neigh_words:
				if neigh not in visited:
					queue.append((neigh, steps + 1))
					visited.add(neigh)

	return 0


if __name__ == '__main__':
	beginWord = "hit"
	endWord = "cog"
	wordList = ["hot", "dot", "dog", "lot", "log", "cog"]

	print ladderLength(beginWord, endWord, wordList)
