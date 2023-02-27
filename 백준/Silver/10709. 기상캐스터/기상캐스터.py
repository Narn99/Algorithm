# 기상 캐스터
# 구름 위치를 알려주고, 1분마다 오른쪽으로 1칸씩 이동

H, W = map(int,input().split())

arr = [input() for _ in range(H)]
v = [[-1]*W for _ in range(H)]

for i in range(H) :
    for j in range(W) :
        if arr[i][j] == 'c' :   # 구름을 찾으면 visit을 0으로 바꾸고,
            v[i][j] = 0
            cj = j
            while True :
                nj = cj+1
                if 0 <= nj < W and arr[i][nj] != 'c' :  # 오른쪽으로 가며 바꿔줌
                    v[i][nj] = v[i][cj] + 1     # 범위 밖으로 가거나, 다른 구름 만나면 종료
                    cj = nj
                else :
                    break

for i in range(H) :
    print(' '.join(map(str, v[i])))