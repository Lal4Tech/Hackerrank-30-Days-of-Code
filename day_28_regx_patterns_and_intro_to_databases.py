#!/bin/python3

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    N = int(input().strip())

    name_list = []
    for N_itr in range(N):
        first_multiple_input = input().rstrip().split()

        firstName = first_multiple_input[0]
        emailID = first_multiple_input[1]
        
        if re.search('@gmail.com$', emailID):
            name_list.append(firstName)
            
    print(*sorted(name_list), sep='\n')