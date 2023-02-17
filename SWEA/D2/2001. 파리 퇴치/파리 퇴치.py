# 파리 퇴치
# NxN 안의 숫자는 파리의 수, MxM의 파리채를 내리쳐 최대한 많은 파리를 죽이기
# => NxN 안에서 MxM의 범위 안의 수가 가장 큰 곳 찾기
# NxN 안에서 행마다 i:i+M, 그리고 j:j+M으로 순회해서 합이 제일 큰 값 찾기?
 
T = int(input())
 
for case in range(T) :
 
    N, M = map(int,input().split())
    Nlst = [list(map(int,input().split())) for _ in range(N)]
    ans = 0
 
    for row in range(N-M+1) :       # 행 별로 M개, 열 별로 M개씩 묶은 사각형의 요소들을 뽑아서
        for col in range(N-M+1) :   # check에 더하고, 그게 현재 최댓값보다 크면 갱신
            check = 0
            for i in range(M) :
                for j in range(M) :
                    check += Nlst[row+i][col+j]
            if check > ans :
                ans = check
 
    print(f'#{case+1} {ans}')