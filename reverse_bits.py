#!/usr/bin/env python
'''
Reverse bits of a given 32 bits unsigned integer.

The idea is keep swapping the first and the last bit of the integer and thus reverse the bits, much like reversing a string
'''
def reverseBits(n):
     
    total = 32
    for i in range(total / 2):
	    n =  swapBits(n, i, total - i - 1)

    return n

        

def swapBits(n, i, j):
    low = (n >> i) & 1
    high = (n >> j) & 1
    
    if low ^ high == 1:
        n ^= ((1 << i) | (1 << j))

    return n



##################### Alternate Solution
'''
Step 1: Take eacb bit (from LSB) and 'AND' with mask
Step 2: Move mask 1 bit to the left (<<) in each iteration
Step 3: The next step is to convert bits back into integer. Bit shift is all we need. "<< " shifts 1 bit left. (Remember if you shift left on an unsigned int by K bits, this is equivalent to multiplying by 2^K.)
In this problem, we check the original int from the lowest bit to highest, 
so the first bit in the original int is the highest bit in the result int. 
By shifting the final int 1 bit each time, the final int after 31 (32-1) times shifting,
it becomes the reverse int of the original int.  32 is the length of the int data type in this problem.

'''



# @param n, an integer
# @return an integer
def reverseBits(self, n):
    res = 0
    mask = 1
    
    for i in range(32):
        if n & mask:
            res += 1
        
        mask <<= 1
        
        if i < 31:              # for last digit, don't shift!
            res <<= 1
                                                                                                                                        
    return res



#############Bonus question 
How to optimize if this function is called multiple times? We can divide an int into 4 bytes, and reverse each byte then combine into an int. For each byte, we can use cache to improve performance.


class Solution {
public:
    uint32_t reverseBits(uint32_t n) {
        n = (n >> 16) | (n << 16);
        n = ((n & 0xff00ff00) >> 8) | ((n & 0x00ff00ff) << 8);
        n = ((n & 0xf0f0f0f0) >> 4) | ((n & 0x0f0f0f0f) << 4);
        n = ((n & 0xcccccccc) >> 2) | ((n & 0x33333333) << 2);
        n = ((n & 0xaaaaaaaa) >> 1) | ((n & 0x55555555) << 1);
        return n;
    }
};




for 8 bit binary number abcdefgh, the process is as follow:

abcdefgh -> efghabcd -> ghefcdab -> hgfedcba
