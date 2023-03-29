
import sys
from collections import deque

di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]

def BFS(Q) :      # 고슴도치가 움직이는 BFS
    global ans

    for i in range(len_q) :
        ci, cj = Q.popleft()

        if arr[ci][cj] == 'D' :
            ans = cnt

        for k in range(4) :
            ni, nj = ci+di[k], cj+dj[k]
            if 0<=ni<R and 0<=nj<C :
                if arr[ni][nj] != '*' and arr[ni][nj] != 'X' :
                    if v[ni][nj] == 0 :
                        v[ni][nj] = 1
                        Q.append((ni, nj))

def flood(lst) :        # 홍수가 움직이는 BFS
    len_w = len(water)
    for i in range(len_w) :
        ci, cj = water.popleft()
        for k in range(4) :
            ni, nj = ci+di[k], cj+dj[k]
            if 0<=ni<R and 0<=nj<C :
                if v[ni][nj] != -1 :        # 물도 방문 확인
                    if arr[ni][nj] == '.' or arr[ni][nj] == 'S' :
                        v[ni][nj] = -1
                        water.append((ni, nj))

R, C = map(int, sys.stdin.readline().split())
arr = [sys.stdin.readline().rstrip() for _ in range(R)]
v = [[0]*C for _ in range(R)]
water = deque()
Q = deque()

for i in range(R) :         # 시작점, 물 시작 위치, 돌 위치, 도착점 위치 전부 구하기
    for j in range(C) :
        if arr[i][j] == 'S' :
            v[i][j] = 1
            Q.append((i,j))
        elif arr[i][j] == '*' :
            v[i][j] = -1
            water.append((i, j))

ans = 'KAKTUS'
cnt = 0

while Q :       # Q가 존재하는 동안, 1턴씩 진행하며 홍수 -> BFS 순으로 진행함
    flood(water)
    len_q = len(Q)
    BFS(Q)
    cnt += 1
    if ans != 'KAKTUS' :
        break

print(ans)