# 파이프 옮기기 1
# BFS로 좌표 따라 가는데, 왼쪽 좌표 하나 기록하고, 방향을 0~2로 가져가기
# 뱀마냥 머리 간 곳에 꼬리가 따라옴.. 3차원 DP로 풀 수 있음..

import sys
from collections import deque



N = int(sys.stdin.readline())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
DP = [[[0]*N for _ in range(N)] for _ in range(3)]
DP[0][0][1] = 1
for j in range(2,N) :
    if arr[0][j] == 1 :     # 맨 윗줄에 1이 있었으면, 거기부터 가로모양 진행 멈춤
        break
    else:
        DP[0][0][j] = DP[0][0][j-1]     # 맨 윗줄은 가로모양 0,1 좌표의 값을 똑같이 따라감

for i in range(1, N) :
    for j in range(1, N) :
        if arr[i-1][j] == 0 and arr[i][j-1] == 0 and arr[i][j] == 0 :  # 대각선일 모양으로 i, j에 도착하는 값
            DP[1][i][j] = DP[0][i-1][j-1] + DP[1][i-1][j-1] + DP[2][i-1][j-1]
        if arr[i][j] == 0 :
            DP[0][i][j] = DP[1][i][j-1] + DP[0][i][j-1]         # 가로 모양으로 i,j에 도착하는 값
            DP[2][i][j] = DP[1][i-1][j] + DP[2][i-1][j]         # 세로 모양으로 i,j에 도착하는 값

ans = 0
for i in range(3) :
    ans += DP[i][N-1][N-1]

print(ans)
