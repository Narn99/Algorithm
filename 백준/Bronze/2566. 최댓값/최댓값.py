# 최댓값
# 9x9 격자판, 81개의 자연수 또는 0이 주어질 때, 최댓값을 찾고, 그 좌표를 구하기

lst = [list(map(int,input().split())) for _ in range(9)]

mx = -1     # 0과 자연수들이 범위니까 0보다 작은 수부터
ans = []

for i in range(9) :
    for j in range(9) :
        if lst[i][j] > mx :
            mx = lst[i][j]
            ans = [i+1, j+1]    # 좌표는 0부터 8까지지만 행렬은 1부터 9임

print(mx)
print(' '.join(map(str,ans)))