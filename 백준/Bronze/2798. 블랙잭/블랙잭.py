# 블랙잭
def dfs(n, sm, cnt) :
    global mx
    if sm > M :
        return
    if cnt > 3 :
        return
    if n == N :
        if cnt == 3 :
            if sm <= M :
                if sm > mx :
                    mx = sm
        return
    dfs(n+1, sm + cards[n], cnt+1)
    dfs(n+1, sm, cnt)

import sys

N , M = map(int,sys.stdin.readline().split())
cards = list(map(int,sys.stdin.readline().split()))

mx = 0
dfs(0, 0, 0)

print(mx)