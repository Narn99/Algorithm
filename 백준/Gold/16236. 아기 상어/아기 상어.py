# 아기 상어
# 상어는 자기보다 큰 물고기가 있는 칸으로는 이동 불가
# 상어는 자기보다 작은 물고기만 먹을 수 있음.
# 먹을 수 있는 가장 가까운 물고기부터 먹으러 감.
# 거리값이 같다면 가장 위에 있는 고기, 그것도 같다면 가장 왼쪽에 있는 고기
# 자기 몸 크기와 같은 수의 물고기를 먹으면 크기가 1 증가
# 매 턴마다 BFS로 가장 짧은 거리의 물고기들을 구하고, 그 중 가장 위, 그 다음 왼쪽 물고기를 먹으러 가기

import sys
from collections import deque

di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]

def BFS(si, sj, big) :
    global check, time, eat, ci, cj
    # global로 while문 돌면서 바뀔 것들 선언

    fishes = []
    Q = deque([(si, sj, 0)])
    v = [[-1]*N for _ in range(N)]
    v[si][sj] = 0
    
    while Q :
        ci, cj, t = Q.popleft()
        # fishes가 있을 때, 들어있는 물고기까지 걸리는 시간이 지금 나온 물고기까지보다 크면 종료..
        if fishes and t > fishes[-1][2] :
            break
        for k in range(4) :
            ni, nj = ci+di[k], cj+dj[k]
            if 0 <= ni < N and 0 <= nj < N :
                if arr[ni][nj] != 0 and arr[ni][nj] < big and v[ni][nj] == -1:
                    fishes.append((ni, nj, t+1))
                    v[ni][nj] = v[ci][cj] + 1
                    # 크기보다 작은 물고기 발견했고, 아직 visit 안 한 곳이면 fishes에 추가
                    # v는 그냥 디버깅 보기 편하려고 +1로 시간 측정
                elif arr[ni][nj] <= big and v[ni][nj] == -1 :
                    v[ni][nj] = v[ci][cj] + 1
                    Q.append((ni, nj, t+1))
                    # 그 외에는 길로서 통과할 수 있으면 추가
    if fishes :
        fishes.sort(key = lambda x: (x[2], x[0], x[1]))
        # 거리, row, col 순으로 정렬해서 가장 가깝고, 위에 있고, 왼쪽에 있는 순으로 정렬
    else :
        # 만약 물고기 없으면 check를 false로 돌리고 종료
        check = False
        return
    # 첫번째 물고기를 꺼내서 잡아먹고, 그 자리로 좌표 이동하고 시간초 추가
    gi, gj, t = fishes[0]
    arr[gi][gj] = 0
    ci, cj = gi, gj
    time += t
    eat += 1
    return



N = int(sys.stdin.readline())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

for i in range(N) :
    for j in range(N) :
        if arr[i][j] == 9 :
            ci, cj = i, j
            arr[i][j] = 0
        # 상어 초기 위치 찾고, 크기 비교에 방해되니 0으로 지워버리기

big = 2
eat = 0
time = 0
check = True

while True :

    BFS(ci, cj, big)

    if not check :
        break
    # check가 false면 while문 종료하고 엄마 상어 부르기
    
    if big == eat :
        big += 1
        eat = 0
    # 먹을만큼 먹었으면 크기 1 키우기
    
print(time)