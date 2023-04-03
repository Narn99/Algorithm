# 보급로
# 도로 배열인 arr와 같은 크기의 v 배열을 만들어서, 각 칸마다 거기까지 가는데의 최소 시간 기록
 
di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]
 
def bfs() :
    while Q :
        ci, cj = Q.pop(0)       # bfs로 인접 칸까지 걸리는 시간의 최솟값을 v에 갱신하며 진행
        for k in range(4) :
            ni, nj = ci+di[k], cj+dj[k]
            if 0<=ni<N and 0<=nj<N :
                if v[ci][cj] + arr[ni][nj] < v[ni][nj] :
                    v[ni][nj] = v[ci][cj] + arr[ni][nj]
                    Q.append((ni,nj))
 
T = int(input())
 
for case in range(1, T+1) :
 
    N = int(input())
    arr = [list(map(int,list(input()))) for _ in range(N)]
    v = [[1e9]*N for _ in range(N)]
 
    Q = [(0, 0)]
    v[0][0] = 0
 
    bfs()
 
    print(f'#{case} {v[N-1][N-1]}')     # bfs 후에 도달점인 v[N-1][N-1] 출력
