# 요리사
# N개의 식재료를 N/2개씩 2명의 손님에게 분배
# 분배된 식재료의 시너지 합의 차이가 최소가 되어야함

def check(n, p1, p2) :
    global ans

    if n == N :
        sm = sm_check(p1, p2)   # 시너지 합의 차이를 계산하고, 현재 ans보다 작다면 갱신
        if sm < ans :
            ans = sm
        return

    else :
        if len(p1) < half :     # p1, p2를 N/2 개수로 채울 때까지 재귀 진행
            check(n+1, p1+[n], p2)
        if len(p2) < half :
            check(n+1, p1, p2+[n])

def sm_check(p1, p2) :
    sm1 = 0
    sm2 = 0
    for i in range(half) :
        for j in range(half) :      # 시너지들의 합을 계산하고 차이를 반환
            if i != j :
                sm1 += arr[p1[i]][p1[j]]
                sm2 += arr[p2[i]][p2[j]]
    return abs(sm1 - sm2)


T = int(input())

for case in range(1, T+1) :

    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]
    ans = 1e9
    half = N//2

    check(0, [], [])

    print(f'#{case} {ans}')