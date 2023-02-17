# 오셀로 게임 ~ 흑은 1, 백은 2 ~ 몇 개인지 세기
# 새로 좌표와 돌을 입력하면, 다른 색을 만날 때까지 가로/세로/대각선을 이어진거 탐색해서 내 색으로 바꿈.
# 함수로 8방향 진행하면서 다른 색을 만나면 스택에 넣어두고, 0을 만나면 색상변경 없으니 스택 비우고 같은 색을 만나면 색을 다 바꿔줌.

dx = [-1, 1, 0, 0, -1, -1, 1, 1]
dy = [0, 0, -1, 1, -1, 1, -1, 1]

def change(ex, ey, color) :
    global stk
    stk += [(ex, ey)]
    if arr[ex+dx[k]][ey+dy[k]] == 0 :           # 0을 만나면 색을 못 바꿔주니 스택 비우기
        stk = []
        return  # 빼먹었던 리턴 추가
    elif arr[ex+dx[k]][ey+dy[k]] == color :     # 같은 색을 만나면 그 색 전까지를 전부 바꿔줌
        while stk :
            a, b = stk.pop()
            arr[a][b] = color
        return
    else :
        return change(ex+dx[k],ey+dy[k],color)  # 다른 색이라면 그 다음 탐색하러


T = int(input())

for case in range(1, T+1) :

    N, M = map(int,input().split())
    arr = [[0]*(N+2) for _ in range(N+2)]     # 패딩 겹겹

    # 초기 배치
    arr[(N+2)//2][(N+2)//2] = 2
    arr[(N+2)//2-1][(N+2)//2-1] = 2
    arr[(N+2)//2-1][(N+2)//2] = 1
    arr[(N+2)//2][(N+2)//2-1] = 1

    for i in range(M) :
        x, y, color = map(int,input().split())
        ex, ey = x, y
        for k in range(8):
            stk = []
            if 0 <= ex+dx[k] < N+2 and 0 <= ey+dy[k] < N+2 :
                change(ex, ey, color)    # 보드범위 내에서 같은 색을 만날 때까지 색을 바꿔준다.

    B, W = 0, 0

    for i in range(len(arr)) :
        for j in range(len(arr[i])) :
            if arr[i][j] == 1 :         # 흑백 개수 세기
                B += 1
            elif arr[i][j] == 2 :
                W += 1

    print(f'#{case} {B} {W}')
