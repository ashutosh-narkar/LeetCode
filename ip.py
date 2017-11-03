#!/usr/bin/env python
'''
Check if a String is a IP address
'''

import sys
import socket


def main():
   
    data = sys.argv[1]
    
    res = is_ip(data)
    if res:
        print '{} is a valid IP'.format(sys.argv[1])
    else:
        print '{} is not a valid IP'.format(sys.argv[1])
        

def is_ip_2(data):

    try:
        socket.inet_aton(data)
        #socket.inet_pton(socket.AF_INET6, data) for ipv6
    except socket.error:
        return False
    
    return True


def is_ip(data):
    """
    Find is a string is a valid IP
    """

    if len(data.split('.')) != 4:
        return False

    for item in data.split('.'):
        if len(item) > 3:
            return False
        try:
            if not 0 <= int(item) <= 255:
                return False
        except ValueError, e:
            return False

    return True    


if __name__ == '__main__':
    main()
