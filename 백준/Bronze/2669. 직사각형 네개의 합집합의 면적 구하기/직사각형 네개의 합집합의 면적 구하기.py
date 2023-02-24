# 직사각형 네개의 합집합의 면적 구하기
# 배열 만들고, 사각형 놓는 자리들은 +1씩 해서, 0이 아닌 곳의 면적을 구하면 될 듯
# x, y 좌표라서 평소 하던 행렬이면 j, i로 받아들여야함

arr = [[0]*101 for _ in range(101)]
ans = 0

for _ in range(4) :
    a, b, c, d = map(int, input().split())
    for i in range(b, d) :
        for j in range(a, c) :
            arr[i][j] += 1      # 직사각형 지점에 1씩 더해주기

for i in range(101) :
    for j in range(101) :
        if arr[i][j] != 0 :
            ans += 1            # 0 아닌 곳들 세기

print(ans)