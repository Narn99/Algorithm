# 곱셈

import sys

def check(b) :
    if b == 1 :
        return A % C
    if b % 2 == 0 :
        next = check(b//2)
        return (next * next) % C
    else :
        next = check((b-1)//2)
        return (next * next * A) % C

A, B, C = map(int, sys.stdin.readline().split())

ans = check(B)

print(ans)

