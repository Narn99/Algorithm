# 숨바꼭질
# X-1이나 X+1로 이동하는 경우, 2*X의 위치로 이동하는 경우의 3가지로 재귀

import sys
from collections import deque

def check(N, K) :
    Q = deque()
    Q.append(N)
    v = [0]*100001

    while Q :
        now = Q.popleft()
        if now == K :
            print(v[now])
            return
        for i in (now-1, now+1, now*2) :
            if i >= 0 and i <= 100000 and v[i] == 0 :
                v[i] = v[now]+1
                Q.append(i)
    return

N, K = map(int, sys.stdin.readline().split())

check(N, K)
