# 2048
# 최대 5번 움직이는거고 4방향이니까, 모든 경우의 수를 따져도 4의 5승밖에 안 됨.
# 그러니 모든 경우의 수를 따져보는거? 배열 다 움직여서?
# 1번 움직일 때마다 나머지 4방향도 탐색하기.
# 해당 위치가 0이 아니라면 다음 것부터 봐서 합쳐지는지, 안 합쳐지는지 판단해서 배치하고 다음 칸 이동
# 해당 위치가 0이라면 그 자리에 그냥 다음에 있는 숫자 옮겨오기

from copy import  deepcopy
import sys

def check(n, board) :
    global ans

    # 5번 다 하면 최댓값 갱신
    if n == 5 :
        for i in range(N) :
            for j in range(N) :
                ans = max(ans, board[i][j])
        return

    # 왼쪽 방향
    tmp1 = deepcopy(board)
    ci = cj = 0

    # ci, cj가 0인 곳에서부터 j에 1을 더해가며 합치고 옮긴다.
    # 만약 cj가 끝까지 도달하면 ci에 1을 더해 다음 행으로 이동하고, cj를 0으로 초기화한다.
    # 마지막 행에 도달하면 종료.
    while True :
        if ci >= N :
            break
        elif cj >= N :
            ci += 1
            cj = 0

        # 좌표가 ci, cj인 곳의 값이 0이 아니라면,
        elif tmp1[ci][cj] != 0 :
            mj = cj+1
            while True :
                if mj >= N :
                    ci += 1
                    cj = 0
                    break
                if tmp1[ci][mj] != 0 :
                    # 같은 숫자면 합쳐주기
                    if tmp1[ci][mj] == tmp1[ci][cj] :
                        tmp1[ci][cj] *= 2
                        tmp1[ci][mj] = 0
                        cj += 1
                        break
                    # 다른 숫자면 바로 다음 칸으로 이동 시켜주기
                    else :
                        tmp1[ci][cj+1] = tmp1[ci][mj]
                        if cj+1 != mj :
                            tmp1[ci][mj] = 0
                        cj += 1
                        break
                mj += 1
        # ci, cj가 좌표인 곳의 값이 0이라면,
        # 0 아닌 값이 있는 곳 찾거나 끝에 도달할 때까지 찾아보고,
        # 없었으면 다음 행으로 이동. 있었으면 그걸 현재 위치로 이동시킴.
        else :
            mj = cj+1
            while True :
                if mj >= N :
                    ci += 1
                    cj = 0
                    break
                elif tmp1[ci][mj] != 0 :
                    tmp1[ci][cj] = tmp1[ci][mj]
                    tmp1[ci][mj] = 0
                    break
                mj += 1
    check(n+1, tmp1)

    # 위쪽 방향도 같은 방식
    tmp2 = deepcopy(board)
    ci = cj = 0

    while True :
        if cj >= N :
            break
        elif ci >= N :
            cj += 1
            ci = 0

        elif tmp2[ci][cj] != 0 :
            mi = ci+1
            while True :
                if mi >= N :
                    cj += 1
                    ci = 0
                    break
                if tmp2[mi][cj] != 0 :
                    if tmp2[mi][cj] == tmp2[ci][cj] :
                        tmp2[ci][cj] *= 2
                        tmp2[mi][cj] = 0
                        ci += 1
                        break
                    else:
                        tmp2[ci+1][cj] = tmp2[mi][cj]
                        if ci+1 != mi :
                            tmp2[mi][cj] = 0
                        ci += 1
                        break
                mi += 1
        else :
            mi = ci+1
            while True :
                if mi >= N :
                    cj += 1
                    ci = 0
                    break
                elif tmp2[mi][cj] != 0 :
                    tmp2[ci][cj] = tmp2[mi][cj]
                    tmp2[mi][cj] = 0
                    break
                mi += 1
    check(n+1, tmp2)

    # 오른쪽 방향
    tmp3 = deepcopy(board)
    ci = cj = N-1

    while True :
        if ci < 0 :
            break
        elif cj < 0 :
            ci -= 1
            cj = N-1

        elif tmp3[ci][cj] != 0 :
            mj = cj-1
            while True :
                if mj < 0 :
                    ci -= 1
                    cj = N-1
                    break
                if tmp3[ci][mj] != 0 :
                    if tmp3[ci][mj] == tmp3[ci][cj] :
                        tmp3[ci][cj] *= 2
                        tmp3[ci][mj] = 0
                        cj -= 1
                        break
                    else :
                        tmp3[ci][cj-1] = tmp3[ci][mj]
                        if cj-1 != mj:
                            tmp3[ci][mj] = 0
                        cj -= 1
                        break
                mj -= 1
        else :
            mj = cj-1
            while True :
                if mj < 0 :
                    ci -= 1
                    cj = N-1
                    break
                elif tmp3[ci][mj] != 0 :
                    tmp3[ci][cj] = tmp3[ci][mj]
                    tmp3[ci][mj] = 0
                    break
                mj -= 1
    check(n+1, tmp3)

    # 아래쪽 방향
    tmp4 = deepcopy(board)
    ci = cj = N-1

    while True :
        if cj < 0 :
            break
        elif ci < 0 :
            cj -= 1
            ci = N-1

        elif tmp4[ci][cj] != 0 :
            mi = ci-1
            while True :
                if mi < 0 :
                    cj -= 1
                    ci = N-1
                    break
                if tmp4[mi][cj] != 0 :
                    if tmp4[mi][cj] == tmp4[ci][cj] :
                        tmp4[ci][cj] *= 2
                        tmp4[mi][cj] = 0
                        ci -= 1
                        break
                    else :
                        tmp4[ci-1][cj] = tmp4[mi][cj]
                        if ci-1 != mi :
                            tmp4[mi][cj] = 0
                        ci -= 1
                        break
                mi -= 1
        else :
            mi = ci-1
            while True :
                if mi < 0 :
                    cj -= 1
                    ci = N-1
                    break
                elif tmp4[mi][cj] != 0 :
                    tmp4[ci][cj] = tmp4[mi][cj]
                    tmp4[mi][cj] = 0
                    break
                mi -= 1
    check(n+1, tmp4)



N = int(sys.stdin.readline())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
ans = 0

check(0, board)

print(ans)