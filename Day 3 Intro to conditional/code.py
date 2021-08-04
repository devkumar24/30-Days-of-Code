#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    N = int(input().strip())
    if (N % 2) != 0:
        print("Weird")
    else :
        if (N % 2) == 0 and N <= 5 and N >= 2:
            print("Not Weird")
        
        else:
            if (N % 2) == 0 and N <= 20 and N >= 6:
                print("Weird")
            else:
                print("Not Weird")
                