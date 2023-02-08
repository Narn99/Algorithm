N = int(input())
lst = list(map(int,input().split()))
cnt = N

for i in lst :
    if i == 1 :                 # 어차피 1은 소수 아니니까 있다면 빼준다
        cnt -= 1
        continue
    for j in range(2, i) :      # 2부터 i-1까지 i를 나누어떨어트리는 j값이 있다면, cnt에서 1 빼기
        if i % j == 0 :
            cnt -= 1
            break

print(cnt)