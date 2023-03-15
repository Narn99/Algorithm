# 연속합

import sys

N = int(sys.stdin.readline())
Nlst = [[0] for _ in range(N)]
lst = list(map(int, sys.stdin.readline().split()))


Nlst[0] = lst[0]
for i in range(1, N) :       # 이전꺼와 현재꺼의 합과 , 현재꺼를 비교해서 현재가 더 크다면 갱신
    Nlst[i] = max(Nlst[i-1]+lst[i], lst[i])

print(max(Nlst))