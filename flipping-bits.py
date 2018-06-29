#!/bin/python
"""
You will be given a list of 32 bit unsigned integers. Flip all the bits (1->0 and 0->1) and print the result as an unsigned integer.

Input Format

The first line of the input contains , the number of test cases.
The next lines each contain an integer to process.

Constraints


Output Format

Output one line per element from the list with the decimal value of the resulting unsigned integer.

Sample Input 0

3
2147483647
1
0

Sample Output 0

2147483648
4294967294
4294967295

Explanation 0

2147483647 = 01111111111111111111111111111111
             10000000000000000000000000000000 = 2147483648

         1 = 00000000000000000000000000000001
             11111111111111111111111111111110 = 4294967294

         0 = 00000000000000000000000000000000
             11111111111111111111111111111111 = 4294967295

"""
import math
import os
import random
import re
import sys

# Complete the flippingBits function below.
def flippingBits(N):
    return ~N & 0xFFFFFFFF

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    T = int(raw_input())
    assert (T >= 1 and T <= 100), "Input must be between 1 and 100."

    for T_itr in xrange(T):
        N = int(raw_input())
        # assert(N >= 0 and N <= 2^32), "Input must be between 0 and 2^32."
        result = flippingBits(N)

        fptr.write(str(result) + '\n')

    fptr.close()
