# 장훈이의 높은 선반
# 점원들의 키를 합쳐서 B를 넘는 값 중 최솟값 구하기.
# 백트래킹으로 합이 B를 넘는 값을 구해서 그 중 최솟값 갱신하기.

def check(n, sm) :
    global ans
    if sm >= B :
        if sm < ans :
            ans = sm
        return
    if n == N :
        return
    else :
        check(n+1, sm + lst[n])
        check(n+1, sm)

T = int(input())

for case in range(1, T+1) :
    N, B = map(int, input().split())
    lst = list(map(int, input().split()))
    ans = 10000000
    check(0, 0)

    print(f'#{case} {ans-B}')