# 숫자 카드
def check(n, s, e) :
    while s <= e :
        p = (s+e)//2
        if n == Nlst[p] :
            return '1'
        elif n > Nlst[p] :
            s = p+1
        else :
            e = p-1
    return '0'

import sys

N = int(sys.stdin.readline().rstrip())
Nlst = list(map(int,sys.stdin.readline().split()))
M = int(sys.stdin.readline().rstrip())
Mlst = list(map(int,sys.stdin.readline().split()))
Nlst.sort()

ans = []

for i in Mlst :
    ans += [check(i, 0, N-1)]

print(' '.join(ans))