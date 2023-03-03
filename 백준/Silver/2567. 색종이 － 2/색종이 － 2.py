# 색종이 - 2
# 100*100 범위에 10*10인 검은 색종이를 여럿 붙이고, 그 둘레를 구하기.
# 1을 찾고, 그 좌표의 4방향 탐색으로 0이 있는 개수만큼 카운팅하면 그게 둘레
# 0과 1이 맞닿은 변 = 길이 1만큼이니까, 0이 만약 2개 맞닿아있다면, 길이 2만큼 적용되는 녀석

di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]

N = int(input())
arr = [[0]*100 for _ in range(100)]

for paper in range(N) :
    left, down = map(int,input().split())
    for row in range(10) :
        arr[down+row][left:left+10] = [1]*10
cnt = 0
for i in range(100) :
    for j in range(100) :
        if arr[i][j] == 1 :
            for k in range(4) :
                ni, nj = i+di[k], j+dj[k]
                if 0<=ni<100 and 0<=nj<100 :
                    if arr[ni][nj] == 0 :
                        cnt += 1
                else :
                    cnt += 1    # 도화지 밖으로 나가면 무조건 둘레

print(cnt)
