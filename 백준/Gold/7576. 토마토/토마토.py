# 토마토
# 익은 토마토가 인접 안 익은 토마토를 하루 지나면 익게 함. 전부 언제 익는가?
# 익은 토마토 전부 넣은 큐로 BFS 돌리면서, v에 며칠인지 기록하기?

import sys
from collections import deque

di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]

M, N = map(int, sys.stdin.readline().split())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
v = [[-1]*M for _ in range(N)]  # v에 일자 기록할거니까 처음부터 익은 토마토는 v에 0으로 기록할거
tomatoes = deque()
for i in range(N) :
    for j in range(M) :
        if arr[i][j] == 1 :
            deque.append(tomatoes, (i,j))
            v[i][j] = 0
if len(tomatoes) == N*M :   # 만약 토마토가 전부 익었으면 0 출력
    print(0)
else :

    while tomatoes :        # BFS
        ci, cj = deque.popleft(tomatoes)
        for k in range(4) :
            ni, nj = ci+di[k], cj+dj[k]
            if 0<=ni<N and 0<=nj<M :
                if arr[ni][nj] == 0 and v[ni][nj] == -1 :
                    v[ni][nj] = v[ci][cj] + 1
                    arr[ni][nj] = 1             # v에 걸린 일자 기록 & arr에 익었다고 바꿔줌
                    deque.append(tomatoes, (ni,nj))
    ans = 0
    for i in range(N) :
        if 0 in arr[i] :    # 다 안 익은게 있으면 -1 출력
            ans = -1
            break
        else :
            imax = max(v[i])    # 걸린 일자 최댓값 갱신
            if imax > ans :
                ans = imax
    print(ans)
