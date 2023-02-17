# 어디에 단어가 들어갈 수 있을까 ~ 델타?
 
T = int(input())
 
for case in range(T) :
 
    N , K = map(int,input().split())
    puzzle = [list(map(int,input().split())) for _ in range(N)]
    result = 0
 
    for i in range(N) :                 # 행에서 K개 연속인걸 구하는 것
        for j in range(N-K+1) :
            sump = 0                   # 연속한 K개의 수가~ 이므로 K개로 묶는다. 고로 N-K+1개 순회
            for k in range(K):
                sump += puzzle[i][j+k]
            if sump == K :
                if j > 0 and j+K < N :
                    if puzzle[i][j-1] == 0 and puzzle[i][j+K] == 0:      # 가장자리가 아닌 것들
                        result += 1
                elif j == 0 :
                    if puzzle[i][j+K] == 0 :        # 왼쪽 가장자리
                        result += 1
                elif j+K == N :
                    if puzzle[i][j-1] == 0 :        # 오른쪽 가장자리
                        result += 1
 
    for j in range(N) :                 # 열에서 K개 연속인걸 구하는 것. 행에서 구한거를 반전만 했다.
        for i in range(N-K+1) :
            sump = 0
            for k in range(K):
                sump += puzzle[i+k][j]
            if sump == K :
                if i > 0 and i+K < N :
                    if puzzle[i-1][j] == 0 and puzzle[i+K][j] == 0:
                        result += 1
                elif i == 0 :
                    if puzzle[i+K][j] == 0 :
                        result += 1
                elif i+K == N :
                    if puzzle[i-1][j] == 0 :
                        result += 1
 
    print(f'#{case+1} {result}')