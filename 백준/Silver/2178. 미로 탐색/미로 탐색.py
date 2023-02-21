# 미로 탐색  ~  BFS 쓰는거라니까 배우고 풀자

N, M = map(int,input().split()) # 밖으로 못 나가게 0으로 감싸기
arr = [[0]*(M+2)] + [[0] + list(map(int,list(str(input()))))+[0] for _ in range(N)] + [[0]*(M+2)]

di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]
cnt = 1
Q = [(1,1,cnt)]
visited = [[0]*(M+2) for _ in range(N+2)]

while True :
    if Q : ci, cj, cnt = Q.pop(0)
    if (ci, cj) == (N, M) :     # 도달하면 종료
        break
    for k in range(4) :
        ni, nj = ci+di[k], cj+dj[k]
        if arr[ni][nj] == 1 and visited[ni][nj] == 0 :
            Q.append((ni, nj, cnt+1))
            visited[ni][nj] = 1     # 방문 기록

print(cnt)