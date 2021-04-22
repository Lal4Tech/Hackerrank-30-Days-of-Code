#!/bin/python3
import math
import os
import random
import re
import sys

if __name__ == '__main__':
    n = int(input())
    binary = bin(n)
    max_count = 0
    while n != 0:
        n = n & (n << 1)
        max_count += 1
    print(max_count)