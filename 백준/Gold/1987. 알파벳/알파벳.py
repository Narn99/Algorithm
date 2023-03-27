# 알파벳
# 상하좌우 한 칸씩 이동 가능한데, 같은 알파벳이 적힌 칸을 두 번 지날 수 없음.
# 지금 지나온 길의 방문한 알파벳을 기록하면서 비교해야됨. 시작점은 0,0
# DFS로 끝까지 탐색하면서 몇 칸 이동했는지? 재귀?

import sys

di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]

def dfs(ci, cj, v) :
    global ans
    for k in range(4) :
        ni, nj = ci+di[k], cj+dj[k]
        if 0 <= ni <= R-1 and 0 <= nj <= C-1 :
            if arr[ni][nj] not in v :
                dfs(ni, nj, v + arr[ni][nj])
    if len(v) > ans :
        ans = len(v)

R, C = map(int, sys.stdin.readline().split())
arr = [sys.stdin.readline().rstrip() for _ in range(R)]
ans = 0
dfs(0, 0, arr[0][0])

print(ans)