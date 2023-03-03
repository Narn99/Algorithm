# 미로2 ~ 4방향 길 찾기. 도착점까지 길이 있는지 판단하기.
# BFS든 DFS든, visit에 넣으면서 나아가고 골에 도착하면 있고, 못 하고 다 pop해버리면 끝
 
di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]
 
def BFS(si, sj) :
    Q = [(si, sj)]
    visit = [[0]*100 for _ in range(100)]
 
    while Q :               # Q에 pop할게 없으면 종료
        ci, cj = Q.pop(0)
        visit[ci][cj] = 1
        if maze[ci][cj] == 3 :  # 골 도착하면 1 반환
            return 1
        for k in range(4) :
            ni, nj = ci+di[k], cj+dj[k]
            if 0 <= ni < 100 and 0 <= nj < 100 :
                if maze[ni][nj] != 1 and visit[ni][nj] == 0 :
                    Q.append((ni, nj))
    return 0    # while문 끝남 = 골에 도달 못 함 = 0 반환
 
T = 10
 
for case in range(1, T+1) :
 
    tc = int(input())
    maze = [list(map(int,list(input()))) for _ in range(100)]
 
    for i in range(100) :
        for j in range(100) :
            if maze[i][j] == 2 :
                si, sj = i, j
 
    ans = BFS(si, sj)
 
    print(f'#{tc} {ans}')