#!/bin/python3

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    n = int(input())
    phone_book = {}
    for i in range(n):
        name, phone = input().split()
        phone_book[name] = phone
    
    while True:
        try:
            name = input()
            if name in phone_book:
                print(name + "=" + phone_book[name])
            else:
                print("Not found")
        except EOFError as e:
            break