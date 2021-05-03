#!/bin/python3

import sys

n = int(input().strip())
a = list(map(int, input().strip().split(' ')))

total_swaps = 0

for i in range(n):
    # Track number of elements swapped during a single array traversal
    swaps_count = 0
    for j in range(n - 1):
        # Swap adjacent elements if they are in decreasing order
        if a[j] > a[j + 1]:
            a[j], a[j + 1] = a[j + 1], a[j]
            swaps_count += 1
    
    total_swaps += swaps_count
    # If no elements were swapped during a traversal, array is sorted
    if swaps_count == 0:
        break

print("Array is sorted in {} swaps.".format(total_swaps))
print("First Element: " + str(a[0]))
print("Last Element: " + str(a[n - 1]))