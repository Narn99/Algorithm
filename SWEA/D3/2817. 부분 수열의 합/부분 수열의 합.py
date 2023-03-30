# 부분 수열의 합

def dfs(n, sm) :
    global ans
    if sm == K :
        ans += 1
        return
    if n == N :
        return
    else :
        dfs(n+1, sm+lst[n])
        dfs(n+1, sm)

T = int(input())

for case in range(1, T+1) :
    N, K = map(int, input().split())
    lst = list(map(int, input().split()))
    ans = 0
    dfs(0, 0)

    print(f'#{case} {ans}')