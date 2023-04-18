# 뱀
# 뱀은 사과를 먹으면 길이가 1씩 늘어나면서 이동하고, 벽이나 자기 자신과 부딪히면 게임 끝
# 머리가 지나가며 visit 처리를 하고, 꼬리가 지나가면서 visit처리를 없애주기.

import sys
from collections import deque

di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

N = int(sys.stdin.readline())   # 보드의 크기 N, 사과의 개수 K, 사과들 apples
K = int(sys.stdin.readline())
apples = [tuple(map(int, sys.stdin.readline().split())) for _ in range(K)]
L = int(sys.stdin.readline())   # 뱀의 방향 변환 횟수 L
change = deque()
for _ in range(L) :
    x, C = sys.stdin.readline().split()
    X = int(x)
    change.append((X, C))

snake = deque([(1,1)])  # 시작 머리 위치
dr = 0      # 시작 방향 (오른쪽)
ci = cj = 1     # 시작 위치
time = 0    # 시간초
v = []      # 방문

while True :
    time += 1
    ni, nj = ci+di[dr], cj+dj[dr]       # 이동할 곳이 보드 안이고,
    if 1<=ni<N+1 and 1<=nj<N+1 and (ni,nj) not in snake :   # 뱀 몸에 안 부딪히면 go
        if (ni, nj) in apples and (ni,nj) not in v :    # 아직 안 먹은 사과 있으면 먹기
            snake.appendleft((ni,nj))
            v.append((ni,nj))
            ci, cj = ni, nj
        else :                          # 사과가 없으면 그대로 이동
            snake.appendleft((ni,nj))
            snake.pop()
            ci, cj = ni, nj
    else :
        break
    if change :                    # 방향 전환해야할 시간이면 방향전환
        if time == change[0][0] :
            if change[0][1] == 'D' :
                dr = (dr+1) % 4
            else :
                dr = (dr-1) % 4
            change.popleft()

print(time)
