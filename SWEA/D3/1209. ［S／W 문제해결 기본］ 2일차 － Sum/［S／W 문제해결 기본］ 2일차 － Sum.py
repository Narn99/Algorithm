T = 10

for case in range(T) :

    test = int(input())

    lst = []
    for i in range(100) :
        lst += [list(map(int,input().split()))]

    maxsum = 0

    for i in range(100) :           # 행에서 최댓값 찾기
        total = 0
        for j in range(100) :
            total += lst[i][j]
        if total > maxsum :
            maxsum = total

    for j in range(100) :           # 열에서 최댓값 찾기
        total =0
        for i in range(100) :
            total += lst[i][j]
        if total > maxsum :
            maxsum = total

    tot = 0
    for i in range(100) :            # 우하향 대각선 최댓값 찾기
        tot += lst[i][i]
    if tot > maxsum :
        maxsum = tot

    tota = 0
    for i in range(100) :            # 우상향 대각선 최댓값 찾기
        tota += lst[i][-i-1]
    if tota > maxsum :
        maxsum = tota

    print(f'#{case+1} {maxsum}')