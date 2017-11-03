#!/usr/bin/env python
'''
Given an absolute path for a file (Unix-style), simplify it.

For example,
path = "/home/", => "/home"
path = "/a/./b/../../c/", => "/c"

Corner Cases:
Did you consider the case where path = "/../"?
In this case, you should return "/".
Another corner case is the path might contain multiple slashes '/' together, such as "/home//foo/".
In this case, you should ignore redundant slashes and return "/home/foo".
'''

def simplifyPath(path):

    path = filter(lambda x: x, path.split('/'))     # for input = '/home//foo' we get ['home', 'foo'] while '/home//foo'.split('\') gives ['', 'home', '', 'foo']
    output = []


    for section in path:
	    if section == '.':
	        continue

	    elif section == '..':
	        if output:
		        output.pop()

	    else:
	        output.append(section)

    return '/' + '/'.join(output)
