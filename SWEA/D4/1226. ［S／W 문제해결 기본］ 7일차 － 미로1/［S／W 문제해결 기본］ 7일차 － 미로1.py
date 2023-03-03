# 미로1
# 16*16 배열, 이미 1로 패딩, 시작점부터 골까지 가기
 
def check() :
    global ans
    while True:
        if Q:
            ci, cj = Q.pop(0)       # 큐에서 pop, 못 하면 종료
        else:
            return
        for (di, dj) in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            ni, nj = ci + di, cj + dj
            if maze[ni][nj] != 1 and v[ni][nj] == 0:
                if (ni, nj) == (ei, ej):
                    ans = 1                 # 다음 지점이 골이면 답 1로 바꾸고 종료
                    return
                Q.append((ni, nj))
                v[ni][nj] = v[ci][cj]+1  # 이동거리 계산하며 배열 변하는거 관찰 재밌음
 
while True :
    try :
        tc = int(input())
        maze = [list(map(int,list(input()))) for _ in range(16)]
        for i in range(16) :
            for j in range(16) :
                if maze[i][j] == 2 :
                    si, sj = i, j
                elif maze[i][j] == 3 :
                    ei, ej = i, j
        ans = 0
        Q = [(si, sj)]
        v = [[0]*16 for _ in range(16)]
        v[si][sj] = 1
 
        check()     # 함수 가동
 
        print(f'#{tc} {ans}')
 
    except :
        break