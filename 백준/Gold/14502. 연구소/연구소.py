# 연구소
# 바이러스와 벽이 있는 지도를 받고, 벽을 3개만 생성해서 2에서 갈 수 있는 0이 최소 개수가 되게 만들기.
# 빈 칸 리스트를 만들고, 거기서 3개를 뽑아서 벽을 세우는 경우를 전부 만들고,
# 2에서부터 BFS를 돌려서 바이러스가 퍼지는게 최소가 되는 경우의 수를 찾기..?

import sys
from collections import deque

di = [-1, 1 ,0, 0]
dj = [0, 0, -1, 1]

def check() :
    global ans
    wall = deque()
    for i in range(le-2) :
        for j in range(i+1, le-1) :
            for k in range(j+1, le) :
                wall.append((empty[i],empty[j],empty[k]))

    for case in wall :
        v = [[0]*M for _ in range(N)]
        cnt = BFS(case, v)
        if le - 3 - cnt > ans :
            ans = le - 3 - cnt

def BFS(case, v) :
    for wall in case :
        v[wall[0]][wall[1]] = 1
    Q = deque([i for i in virus])
    cnt = 0

    while Q :
        ci, cj = Q.popleft()
        for dr in range(4) :
            ni, nj = ci+di[dr], cj+dj[dr]
            if 0<=ni<N and 0<=nj<M :
                if arr[ni][nj] == 0 and v[ni][nj] == 0 :
                    v[ni][nj] = 2
                    cnt += 1
                    Q.append((ni, nj))
    return cnt


N, M = map(int, sys.stdin.readline().split())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

virus = deque()
empty = deque()

for i in range(N) :
    for j in range(M) :
        if arr[i][j] == 2 :
            virus.append((i, j))
        elif arr[i][j] == 0 :
            empty.append((i, j))
ans = 0
le = len(empty)
check()

print(ans)