# 정사각형 방
# N*N 배치된 방, 각 방엔 1부터 N2까지 각자 다른 숫자가 적혀있음.
# 상하좌우로 이동 가능한데, 방이 있어야하며, 그 방의 숫자가 현재 방의 숫자보다 1 커야 이동 가능.
# 어떤 숫자가 적힌 방에서 시작해야 가장 많이 이동할 수 있을까?
 
T = int(input())
 
for case in range(1, T+1) :
 
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]
    mx = 1
    num = N**2
 
    for i in range(N) :
        for j in range(N) :
            ci, cj, cnt = i, j, 1   # 현재 i,j 좌표와 이동한 방 개수 초기화
            while True :
                for di, dj in (-1,0), (1,0), (0,-1), (0,1) :
                    ni, nj = ci+di, cj+dj
                    if 0 <= ni < N and 0 <= nj < N :
                        if arr[ni][nj] == arr[ci][cj]+1 :
                            ci, cj, cnt = ni, nj, cnt+1    # 이동할 때마다 cnt+1
                            break
                else :
                    break
            if cnt > mx :  # 이동 수 최댓값 갱신, 만약 그 시작 방 값이 더 작다면 갱신
                mx = cnt
                num = arr[i][j]
            elif cnt == mx :
                if arr[i][j] < num :
                    num = arr[i][j]
 
    print(f'#{case} {num} {mx}')