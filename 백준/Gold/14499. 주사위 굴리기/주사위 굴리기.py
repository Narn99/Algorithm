# 주사위 굴리기
# 지도의 각 칸에 숫자가 적혀있고, 주사위가 구르며 지도와 맞닿은 바닥면에 지도 칸의 숫자가 복사됨
# 이동할 때마다 상단에 쓰여있는 값을 구하는 프로그램. 시작에 모든 면은 0이 적혀있음.
# 예시와 같이 1번부터 6번까지 주사위 면을 정해놓고, 이동한 뒤의 그 면이 이동한 인덱스들을 구한다.
# 가령 a~e가 0~5였으면, 동으로 한 칸 이동한 뒤에는 3,1,0,5,4,2 순서로 정리되고,
# 그 인덱스의 값들을 새 a~e로 해서 0~5번 순서로 저장해서 다음 차례로 진행한다.

di = [0, 0, 0, -1, 1]
dj = [0, 1, -1, 0, 0]

import sys
from collections import deque

N, M, ci, cj, K = map(int,sys.stdin.readline().split())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
order = deque(list(map(int, sys.stdin.readline().split())))
dice = [0]*6      # 주사위의 값들 기록

while order :
    now = order.popleft()
    ni, nj = ci+di[now], cj+dj[now]
    if 0<=ni<N and 0<=nj<M :
        if now == 1 :       # 각 이동 방향에 따른 인덱스값의 변화를 기록
            a, b, c, d, e, f = 3, 1, 0, 5, 4, 2
        elif now == 2 :
            a, b, c, d, e, f = 2, 1, 5, 0, 4, 3
        elif now == 3 :
            a, b, c, d, e, f = 4, 0, 2, 3, 5, 1
        else :
            a, b, c, d, e, f = 1, 5, 2, 3, 0, 4
        dice[0:6] = [dice[a], dice[b], dice[c], dice[d], dice[e], dice[f]]
        # 변한 인덱스값을 a~f 순서대로 다시 정렬해서 dice에 넣어준다.
        if arr[ni][nj] != 0 :
            dice[5] = arr[ni][nj]   # 이동한 칸의 값이 0이 아니라면 맨 밑의 칸에 복사하고, 칸은 0으로
            arr[ni][nj] = 0
        else :
            arr[ni][nj] = dice[5]   # 칸의 값이 0이었다면 맨 밑의 칸의 값으로 복사
        print(dice[0])
        ci, cj = ni, nj     # 좌표 이동

