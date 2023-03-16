# 쉬운 계단 수
# 리스트에 DP로 경우의 수를 기록해나가며 진행
# 0과 9으로 가는건 1과 8뿐 => 다른거랑 다르게 1곳에서밖에 안 받음
# 한 칸씩 내려가면서 다음 행의 숫자 n에는 n-1과 n+1에서 넘어옴
# 즉 n-1과 n+1까지 온 경우의 수를 합친 값이 n에 들어가는 것
# 그렇게 내려가서, 마지막 행의 합이 모든 경우의 수

N = int(input())
arr = [[0]*10 for _ in range(N+1)]
arr[1][1:] = [1]*9

for i in range(2, N+1) :
    for j in range(10) :
        if j == 0 :
            arr[i][j] = arr[i-1][j+1]
        elif j == 9 :
            arr[i][j] = arr[i-1][j-1]
        else :
            arr[i][j] = arr[i-1][j-1] + arr[i-1][j+1]

print(sum(arr[N]) % 1000000000)