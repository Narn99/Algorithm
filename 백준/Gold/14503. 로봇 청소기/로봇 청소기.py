# 로봇 청소기
# 현재 칸 청소, 주변 4 칸이 다 깨끗하면 1칸 후진, 후진 불가능이면 작동 정지
# 주변 4칸 청소되지 않은 칸이 있다면 반시계 90% 회전 후 앞이 청소 안 됐으면 전진
# 0은 청소 안 된 빈 칸, 1은 벽

import sys

di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]

N, M = map(int,sys.stdin.readline().split())
r, c, d = map(int,sys.stdin.readline().split())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
v = [[0]*M for _ in range(N)]
ans = 0

ci, cj = r, c
while True :
    if v[ci][cj] == 0 :
        v[ci][cj] = 1
        ans += 1
    for k in range(1, 5) :
        dr = (d-k)%4
        ni, nj = ci+di[dr], cj+dj[dr]
        if 0<=ni<N and 0<=nj<M :
            if arr[ni][nj] == 0 and v[ni][nj] == 0 :
                ci, cj = ni, nj
                d = dr
                break
    else :
        if arr[ci+di[d-2]][cj+dj[d-2]] == 0 :
            ci, cj = ci+di[d-2], cj+dj[d-2]
        else :
            break

print(ans)