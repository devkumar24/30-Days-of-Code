#!/bin/python3

import math
import os
import random
import re
import sys

from collections import Counter

if __name__ == '__main__':
    n = int(input().strip())
    freq = 0
    while(n):
        n = n & (n<<1)
        freq += 1
    print(freq)
