import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(raw_input())
    for i in range(1, 11):
        mult = n * i
        print '{n} x {i} = {mult}'.format(n=n, i=i, mult = mult)
