#!/bin/python3

from math import sqrt

def is_prime(num):
    for i in range(2, int(sqrt(num) + 1)):
        if num % i == 0:
            return False
    return True

T = int(input())
for _ in range(T):
    num = int(input())
    if num >= 2 and is_prime(num):
        print('Prime')
    else:
        print('Not prime')