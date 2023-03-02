# 의석이의 세로로 말해요
 
T = int(input())
 
for case in range(1, T+1) :
 
    arr = [list(input()) for _ in range(5)]
    mxl = 0
    for l in arr :
        if len(l) > mxl :
            mxl = len(l)
 
    ans = ''
 
    for j in range(mxl) :
        for i in range(5) :
            try : ans += arr[i][j]
            except : pass
 
    print(f'#{case} {ans}')