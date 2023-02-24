# 탈주범 검거
# 통로가 연결돼있다 = 노드끼리 서로 연결됐다고 볼 수 있긴한데..
# 맨홀은 시작 노드, 경과된 시간동안 지나는 노드의 개수를 세면, 탈주범이 위치할 수 있는 장소의 개수
# 서로 연결이 돼야 갈 수 있음. 방향으로? 방향 이동할 때, 특정 타입이 아니면 이동 못 하게..
# visit에 못 가게 하면, 중간에 루트가 막혀서 못 가니 답이 틀리고,
# visit에 들릴 수 있게 하면 시간 초과가 떠버린다. => 스택을 써서 되돌아가지 못 하게 해보기.

up = [1, 2, 4, 7]
down = [1, 2, 5, 6]
left = [1, 3, 6, 7]
right = [1, 3, 4, 5]

def mov(ci, cj, cnt, stk) :
    if cnt == L: return
    shape = tunnel[ci][cj]

    if shape in up :    # 현재 위치가 위로 갈 수 있을 때
        if 0 <= ci-1 < N and stk[-1] != (ci-1, cj) :  # 이동할 곳이 스택 마지막 항이 아니라면 go
            if tunnel[ci-1][cj] in down :   # 이동할 곳이 갈 수 있는 곳이라면 go
                visit[ci-1][cj] = 1
                stk.append((ci,cj))       # 이동할 때의 스택 비교를 위해서 현재 위치 추가해주기
                mov(ci-1, cj, cnt+1,stk)
                stk.pop()                 # 이동했으면 바로 스택에서 빼주기 (하위 재귀에서만 해당 항 남아있게)
    if shape in down :  # 아래로 갈 수 있을 때
        if 0 <= ci+1 < N and stk[-1] != (ci+1, cj) :
            if tunnel[ci+1][cj] in up :
                visit[ci+1][cj] = 1
                stk.append((ci,cj))
                mov(ci+1, cj, cnt+1, stk)
                stk.pop()
    if shape in left :  # 왼쪽으로 갈 수 있을 때
        if 0 <= cj-1 < M and stk[-1] != (ci, cj-1) :
            if tunnel[ci][cj-1] in right :
                visit[ci][cj-1] = 1
                stk.append((ci,cj))
                mov(ci, cj-1, cnt+1, stk)
                stk.pop()
    if shape in right :  # 오른쪽으로 갈 수 있을 때
        if 0 <= cj+1 < M and stk[-1] != (ci, cj+1) :
            if tunnel[ci][cj+1] in left :
                visit[ci][cj+1] = 1
                stk.append((ci,cj))
                mov(ci, cj+1, cnt+1, stk)
                stk.pop()

T = int(input())

for case in range(1, T+1) :

    N, M, R, C, L = map(int,input().split())
    tunnel = [list(map(int,input().split())) for _ in range(N)]
    si, sj = R, C
    visit = [[0]*M for _ in range(N)]
    visit[si][sj] = 1
    stk = [(si,sj)]
    mov(si,sj,1,stk)

    ans = 0
    for i in range(N) :
        for j in range(M) :
            if visit[i][j] == 1 :
                ans += 1

    print(f'#{case} {ans}')