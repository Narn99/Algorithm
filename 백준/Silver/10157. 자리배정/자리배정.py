# 자리배정
# 1,1부터 위, 오른쪽, 아래, 왼쪽 순으로 돌아가며 자리 배정 (나중에 답에 1씩 더하자)
# 배열을 0을 1로 바꿔가면서 카운팅
import sys

di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

C, R = map(int,sys.stdin.readline().split())
arr = [[0]*R for _ in range(C)]     # 왼쪽 아래를 0,0이라고 놓고 계산하는게 그림
K = int(sys.stdin.readline())       # 그냥 오른쪽으로 90도 회전시켜서 2차 배열로 보자.
i, j = 0, 0                       # 행과 열만 바꾸면 됨
k = 0
if K > C*R : print(0)
else :
    for seat in range(1, C*R+1) :
        if seat == K:
            print(i + 1, j + 1)
            break
        else :
            arr[i][j] = seat
            if 0 <= i+di[k] < C and 0 <= j+dj[k] < R and arr[i+di[k]][j+dj[k]] == 0 :
                i += di[k]
                j += dj[k]
            else :
                k = (k+1) % 4
                i += di[k]
                j += dj[k]
                continue
