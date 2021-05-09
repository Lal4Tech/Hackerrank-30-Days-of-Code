#!/bin/python3

dr, mr, yr = list(map(int, input().split()))
dd, md, yd = list(map(int, input().split()))

if (yr, mr, dr) <= (yd, md, dd):
    print(0)
elif (yr, mr) == (yd, md):
    print(15 * (dr - dd))
elif yr == yd:
    print(500 * (mr - md))
else:
    print(10000)