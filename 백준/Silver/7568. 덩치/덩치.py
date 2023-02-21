# 덩치 ~ x, y가 둘 다 더 크다면 덩치가 크지만, 하나만 크다면 뭐라 못 함

import sys

N = int(sys.stdin.readline().rstrip())
Nlst = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]
rank = []

for i in Nlst :
    cnt = 1
    for j in Nlst :
        if i[0] < j[0] and i[1] < j[1] :
            cnt += 1
    else :
        rank += [cnt]

print(' '.join(map(str,rank)))