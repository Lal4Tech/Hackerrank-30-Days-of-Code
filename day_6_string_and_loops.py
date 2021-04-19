#!/bin/python3

t = int(input())
for i in range(t):
    s = input()
    l = len(s)
    fs = "".join([s[j] for j in range(0, l, 2)])
    ss = "".join([s[j] for j in range(1, l, 2)])
    print(fs + " " + ss)