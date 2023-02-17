# 숫자 배열 회전
# 단순 회전은 인덱스값으로 i랑 j만 전환해도 위치값이 바뀜
 
T = int(input())
 
for case in range(T) :
 
    N = int(input())
    lst = [list(map(int,input().split())) for _ in range(N)]
 
    lst90 = [[0]*N for _ in range(N)]
    lst180 = [[0]*N for _ in range(N)]
    lst270 = [[0]*N for _ in range(N)]
 
    for i in range(N) :         # 회전했을 때의 값을 90도 회전한 리스트에 넣어줌
        for j in range(N) :
            lst90[i][j] += lst[-j-1][i]
 
    for i in range(N) :         # 180도 회전한 리스트에 넣어줌
        for j in range(N) :
            lst180[i][j] += lst[N-i-1][N-j-1]
 
    for i in range(N) :         # 270도 회전한 리스트에 넣어줌
        for j in range(N) :
            lst270[i][j] += lst[j][N-i-1]
 
    print(f'#{case+1}')
    for i in range(N) :         # 한 줄씩 양식에 맞게 출력
        for j in range(N) :
            print(lst90[i][j], end= '')
        print(end=' ')
        for j in range(N) :
            print(lst180[i][j], end= '')
        print(end=' ')
        for j in range(N) :
            print(lst270[i][j], end= '')
        print()
