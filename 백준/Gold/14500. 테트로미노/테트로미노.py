# 테트로미노
# 4칸을 놓아서 수들의 합이 최대로 되는 프로그램
# 걍 dfs같은거로 값이 최대가 되는거 구하기.. 백트래킹

di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]

import sys

def dfs(n, i, j, sm, v) :
    global ans
    if n == 4 :
        if sm > ans :
            ans = sm
        return
    else :
        for k in range(4) :
            ni, nj = i+di[k], j+dj[k]
            if 0<=ni<N and 0<=nj<M :
                if v[ni][nj] == 0:
                    v[ni][nj]=1
                    dfs(n+1, ni, nj, sm+arr[ni][nj], v)
                    v[ni][nj]=0

def bfs(i, j, sm) :
    global ans

    for k in range(4) :
        cnt = sm
        ai, aj = i+di[k], j+dj[k]
        bi, bj = i+di[(k+1)%4], j+dj[(k+1)%4]
        ci, cj = i+di[(k+2)%4], j+dj[(k+2)%4]
        if 0<=ai<N and 0<=aj<M :
            if 0<=bi<N and 0<=bj<M :
                if 0<=ci<N and 0<=cj<M :
                    cnt += arr[ai][aj] + arr[bi][bj] + arr[ci][cj]
        if cnt > ans:
            ans = cnt
    return


N, M = map(int, sys.stdin.readline().split())
arr = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]
ans = 0
v = [[0]*M for _ in range(N)]

for i in range(N) :
    for j in range(M) :
        v[i][j] = 1
        dfs(1, i, j, arr[i][j], v)
        bfs(i, j, arr[i][j])
        v[i][j] = 0

print(ans)