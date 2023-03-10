import bisect
import sys

N = int(sys.stdin.readline())
lst = list(map(int, sys.stdin.readline().split()))

dp = [lst[0]]   # 수열 첫 수로 시작

for i in range(N) :
    if lst[i] > dp[-1] :    # i번째 수가 dp 안의 마지막 수보다 크다면 넣어줌
        dp.append(lst[i])
    else :
        idx = bisect.bisect_left(dp, lst[i])    # 아니라면 i번째 수를 dp 안의 크기 순서에 들어맞게 교체
        dp[idx] = lst[i]

print(len(dp))      # 크기만 구하는거고, 해당 부분수열 자체를 구하는 식은 아님