# 단지번호붙이기 ~ 연결 돼있어야 단지

import sys
from collections import deque


di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]

def BFS(i, j) :         # BFS로 집 개수 세기
    global v
    Q = deque([(i, j)])
    v[i][j] = 1
    cnt = 0

    while Q :
        ci, cj = deque.popleft(Q)
        cnt += 1
        for k in range(4) :
            ni, nj = ci+di[k], cj+dj[k]
            if 0<=ni<N and 0<=nj<N:
                if arr[ni][nj] == '1' and v[ni][nj] == 0 :
                    v[ni][nj] = 1
                    deque.append(Q, (ni,nj))
    return cnt


N = int(sys.stdin.readline())
arr = [sys.stdin.readline().rstrip() for _ in range(N)]

v = [[0]*N for _ in range(N)]

cnt = 0
house = deque()

for row in range(N) :
    for col in range(N) :
        if arr[row][col] == '1' and v[row][col] == 0 :
            house_cnt = BFS(row, col)
            cnt += 1
            deque.append(house, house_cnt)

house = sorted(house)   # 오름차순으로 정렬

print(cnt)
for num in house :
    print(num)