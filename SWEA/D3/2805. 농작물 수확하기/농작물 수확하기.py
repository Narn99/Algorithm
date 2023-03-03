# 농작물 수확하기
# 마름모 형태의 농장에서 수확하여 수익 얻기. 마름모니까 BFS로 풀면 될 듯?
# 농장은 항상 홀수니까 정중앙 인덱스는 N//2, 이동 거리도 N//2
 
di = [-1, 1 ,0, 0]
dj = [0, 0, -1, 1]
 
T = int(input())
 
for case in range(1, T+1) :
 
    N = int(input())
    farm = [list(map(int,list(input()))) for _ in range(N)]
    si, sj = N//2, N//2
 
    Q = [(si,sj)]
    v = [[0]*N for _ in range(N)]
    v[si][sj] = 1
    ans = 0
 
    while Q :               # BFS
        ci, cj = Q.pop(0)
        ans += farm[ci][cj]
        for k in range(4) :
            ni, nj = ci+di[k], cj+dj[k]
            if 0 <= ni < N and 0 <= nj < N :
                if v[ci][cj] <= N//2 and v[ni][nj] == 0 :   # visit에 거리 재면서 이동
                    v[ni][nj] = v[ci][cj] + 1   # 가운데가 1이니, N//2 + 1까지 이동하면 종료
                    Q.append((ni,nj))
 
    print(f'#{case} {ans}')