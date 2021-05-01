#!/bin/python3

class Calculator():
    def power(self, n, p):
        if n | p < 0:
            return ValueError("n and p should be non-negative")
        return n ** p

if __name__ == '__main__':
    myCalculator=Calculator()
    T=int(input())
    for i in range(T):
        n,p = map(int, input().split())
        try:
            print(myCalculator.power(n,p))
        except Exception as e:
            print(e)