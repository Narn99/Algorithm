# 유기농 배추

import sys

di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]

def BFS() :
    cnt = 0
    v = [[0]*M for _ in range(N)]
    for i in range(N) :
        for j in range(M) :
            if arr[i][j] == 1 and v[i][j] == 0 :
                Q = [(i, j)]
                v[i][j] = 1
                while Q :
                    ci, cj = Q.pop(0)       # 배추 묶음마다 cnt 1 추가
                    for k in range(4) :
                        ni, nj = ci+di[k], cj+dj[k]
                        if 0<=ni<N and 0<=nj<M :
                            if arr[ni][nj] == 1 and v[ni][nj] == 0 :
                                v[ni][nj] = 1
                                Q.append((ni,nj))
                cnt += 1
    return cnt

T = int(sys.stdin.readline())

for case in range(1, T+1) :

    M, N, K = map(int, sys.stdin.readline().split())
    arr = [[0]*M for _ in range(N)]
    for _ in range(K) :
        m, n = map(int, sys.stdin.readline().split())
        arr[n][m] = 1   # 배추 위치

    print(BFS())