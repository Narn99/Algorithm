# 최소비용
# 이동시 기본 연료 소모 1, 높이가 높아지면 그 차이만큼 추가 소모
# 만약 다익스트라라고 생각하면, 상하좌우가 인접 노드고, 높이가 가중치...??
# 4방향으로 비교하며, 갱신 가능할 때만 Q에 추가하기
 
from collections import deque
 
di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]
 
def dijkstra() :
    Q = deque([(0, 0)])      # 0,0 좌표
    fuel = [[INF]*N for _ in range(N)]
    fuel[0][0] = 0              # 이동하며 그 칸까지 연료 소비 기록할 것
 
    while Q :
        ci, cj = Q.popleft()
        for k in range(4) :
            ni, nj = ci+di[k], cj+dj[k]
            if 0<=ni<N and 0<=nj<N :   
                h = arr[ni][nj] - arr[ci][cj]   # 높이 비교
                if h > 0 :        # 높이가 더 높은 곳이면 높이차만큼 추가 소모
                    if fuel[ci][cj]+h+1 < fuel[ni][nj] :    # 갱신할 수 있을 때에만 넣어준다.
                        fuel[ni][nj] = fuel[ci][cj]+h+1
                        Q.append((ni, nj))
                else :
                    if fuel[ci][cj]+1 < fuel[ni][nj] :
                        fuel[ni][nj] = fuel[ci][cj]+1
                        Q.append((ni, nj))
    return fuel[N-1][N-1]
 
T = int(input())
 
for case in range(1, T+1) :
 
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    INF = 10000000
 
    ans = dijkstra()
 
    print(f'#{case} {ans}')