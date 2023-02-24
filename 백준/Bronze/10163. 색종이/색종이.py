# 색종이 ~ 색종이 겹쳐 놓기. 각 색종이가 보이는 면적 구하기.
# => 그냥 배열에 그 색종이를 의미하는 수로 덮어씌우기

N = int(input())
arr = [[-1]*1001 for _ in range(1001)]  # 1001*1001 격자

mx_i = 0
mx_j = 0

for paper in range(N) :
    a, b, c, d = map(int,input().split())
    if a+c > mx_i :
        mx_i = a+c      # 시간 줄이기용 범위 구하기 조건
    if b+d > mx_j :
        mx_j = b+d
    for i in range(a, a+c) :
        for j in range(b, b+d) :
            arr[i][j] = paper           # 색종이 붙여주기

ans = []
for paper in range(N) :
    cnt = 0
    for i in range(mx_i) :
        for j in range(mx_j) :
            if arr[i][j] == paper :     # 다 붙인 뒤의 색종이 면적 구해서 기록
                cnt += 1
    else :
        ans.append(cnt)

for i in range(N) :
    print(ans[i])