# 오목 판정
# 세로, 우하향, 가로, 우상향 방향으로 5개 이상 연속한게 있으면 YES, 없으면 NO
 
di = [1, 1, 0, -1]
dj = [0, 1, 1, 1]
 
def check() :
    for j in range(N) :
        for i in range(N) :
            if arr[i][j] == 'o' :       # 돌을 찾으면 세로, 우하향, 가로, 우상향 탐색
                for k in range(4) :     
                    cnt = 1
                    ci, cj = i, j
                    while True :        # 한 방향을 계속 진행해서 연속으로 돌이 있는지 세줌.
                        ni, nj = ci+di[k], cj+dj[k]
                        if 0 <= ni < N and 0 <= nj < N :
                            if arr[ni][nj] != 'o' :  # 돌이 5개 되기 전에 다른게 나오면 탈출
                                break
                            cnt += 1
                            if cnt >= 5 :
                                return 'YES'
                            ci, cj = ni, nj
                        else :
                            break       # 오목판 밖으로 나가면 탈출
    return 'NO'
 
 
T = int(input())
 
for case in range(1, T+1) :
 
    N = int(input())
    arr = [input() for _ in range(N)]
    ans = check()
 
    print(f'#{case} {ans}')