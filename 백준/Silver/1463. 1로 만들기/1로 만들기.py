# 1로 만들기
# X가 3으로 나누어 떨어지면 3, 2로 나누어 떨어지면 2, 1을 빼기
# 여럿 구하고 최솟값

def check(N, cnt) :
    global ans
    if cnt > ans :
        return
    if N == 1 :
        if cnt < ans :
            ans = cnt
        return
    else :
        if N % 3 == 0 :
            check(N//3, cnt+1)
        if N % 2 == 0 :
            check(N//2, cnt+1)
        check(N-1, cnt+1)

N = int(input())
ans = 10**6

check(N, 0)

print(ans)