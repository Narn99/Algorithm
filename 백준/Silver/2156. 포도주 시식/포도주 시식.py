# 포도주 시식
# 연속 3잔 시식 불가

N = int(input())
wine = [0]*10000
for i in range(N) :
    wine[i] = int(input())
sm = [0]*10000

sm[0] = wine[0]
sm[1] = wine[1] + wine[0]
sm[2] = max(sm[1], wine[2] + wine[0], wine[2]+wine[1])

for num in range(3,N) :
    sm[num] = max(wine[num]+sm[num-2], wine[num]+wine[num-1]+sm[num-3], sm[num-1])

print(max(sm))