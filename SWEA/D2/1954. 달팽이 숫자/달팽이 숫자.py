# 달팽이 숫자
# 델타 탐색으로 좌표 이동. 모서리에 부딪히면 (좌표가 N-1 인덱스에 도착하면) 방향전환?
# 오른쪽이 비어있으면 오른쪽으로, 아래가 비어있으면 아래,
# 왼쪽이 비어있으면 왼쪽, 위가 비어있으면 위로,
# 넣어줄 수는 cnt로 세자.
 
T = int(input())
 
for case in range(T) :
 
    N = int(input())
    lst = [[0]*N for _ in range(N)]
 
    cnt = 1
 
    for i in range(N):
        for j in range(i, N-i):         # 오른쪽으로 나아가며 cnt를 넣어줌
            lst[i][j] += cnt
            cnt += 1
        for j in range(i+1, N-i):       # 밑으로 나아가며 cnt를 넣어줌
            lst[j][N - 1 - i] += cnt
            cnt += 1
        for j in range(i+1, N-i):           # 왼쪽으로 나아가며 cnt를 넣어줌
            lst[N - 1 - i][-j - 1] += cnt
            cnt += 1
        for j in range(i+1, N -i - 1):
            lst[-j - 1][i] += cnt           # 위로 나아가며 cnt를 넣어줌
            cnt += 1
 
    print(f'#{case+1}')
    for i in range(len(lst)) :
        for j in range(len(lst[i])) :
            print(lst[i][j], end=' ')
        print()