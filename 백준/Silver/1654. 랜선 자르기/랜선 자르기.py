# 랜선 자르기
# 1 <= num <= lst[0]
# 특정 x로 //한 값을 합친게 N보다 크거나 같아야함.

import sys

K, N = map(int,sys.stdin.readline().split())
lst = [int(sys.stdin.readline()) for _ in range(K)]
lst.sort()

s = 1
e = lst[-1]

while s <= e :
    m = (s+e)//2        # 이진탐색
    cnt = 0
    for num in lst :
        cnt += num//m
    else :
        if cnt >= N :
            s = m+1
        else :
            e = m-1

print(e)