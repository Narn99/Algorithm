# 세제곱근 ~ 이진탐색
 
def check(N) :
    global ans
    s, e = 0, N
    while s <= e:
        m = (s+e)//2
        if m**3 == N : ans = m; return
        elif m**3 > N : e = m-1
        else : s = m+1
 
T = int(input())
 
for case in range(1, T+1) :
 
    N = int(input())
    ans = -1
    check(N)
 
    print(f'#{case} {ans}')