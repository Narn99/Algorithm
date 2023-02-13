# 카운팅 정렬

import sys

N = int(sys.stdin.readline().rstrip())
cnt = [0] * 10001

for i in range(N) :
    cnt[int(sys.stdin.readline().rstrip())] += 1

for i in range(10001) :
    if cnt[i] != 0 :
        for j in range(cnt[i]) :
            print(i)