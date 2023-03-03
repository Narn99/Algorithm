# 러시아 국기 같은 깃발
# 그냥 모든 경우의 수를 계산하는건데, **중복이 없으니까.**
# ** 흰색이 0부터 N-2까지 가능한 i, 파랑은 i+1부터 N-1까지 가능한 j, 빨강은 j+1부터 N까지.
# 그 각각 범위의 W, B, R을 세주고, 그게 최대가 되는 값을 구해서 N*M에서 빼면 그게 변화의 최소값.
 
T = int(input())
 
for case in range(1, T+1) :
 
    N, M = map(int,input().split())
    flag = [list(input()) for _ in range(N)]
    ans = 0
 
    for i in range(0, N-2) :
        for j in range(i+1, N-1) :
            cnt = 0
            for s in range(0, i+1) :
                cnt += flag[s].count('W')
            for s in range(i+1, j+1) :
                cnt += flag[s].count('B')
            for s in range(j+1, N) :
                cnt += flag[s].count('R')
            ans = max(ans, cnt)
 
    print(f'#{case} {N*M - ans}')