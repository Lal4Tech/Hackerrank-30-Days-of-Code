#!/bin/python3
import math
import os
import random
import re
import sys

if __name__ == '__main__':
    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))
        
    print(max([sum(arr[i-1][j-1:j+2] + [arr[i][j]] + arr[i+1][j-1:j+2]) for j in range(1, 5) for i in range(1, 5)]))
