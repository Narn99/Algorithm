# 색종이 ~ 색종이 겹쳐 놓기. 각 색종이가 보이는 면적 구하기.
# => 그냥 배열에 그 색종이를 의미하는 수로 덮어씌우기

import sys

N = int(sys.stdin.readline().rstrip())
arr = [[0]*1001 for _ in range(1001)]  # 1001*1001 격자
Nlst = [0]
ans = [0]

for paper in range(1, N+1) :
    a, b, c, d = map(int,sys.stdin.readline().split())
    Nlst.append([a,b,c,d])  # 색종이 정보 기록
    for i in range(a, a+c) :
        arr[i][b:b+d] = [paper]*d           # 색종이 붙여주기

for paper in range(1, N+1) :
    cnt = 0
    a, b, c, d = map(int, Nlst[paper])
    for i in range(a, a+c) :    # 시간 줄이기 위해 기록해뒀던 원래 색종이 붙인 범위 내만 탐색
        for j in range(b, b+d) :
            if arr[i][j] == paper :     # 다 붙인 뒤의 색종이 면적 구해서 기록
                cnt += 1
    else :
        ans.append(cnt)

for i in range(1, N+1) :
    print(ans[i])