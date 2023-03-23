# 평범한 배낭
# K만큼 넣을 수 있는 배낭에, 최대한 물건을 넣어 최대 가치를 얻기.
# 냅색 알고리즘, 한 번 공부해보고 풀기

import sys

N, K = map(int,sys.stdin.readline().split())
DP = [0]*(K+1)          # 0 ~ K까지 무게를 나타낼 수 있는 DP 1차 배열 작성.

for i in range(N) :
    W, V = map(int, sys.stdin.readline().split())   # 물건 순회하며 무게가 K보다 작은 물건이라면,
    if W <= K :
        for j in range(K, W-1, -1) :    # 앞에서부터 하면 갱신된 값으로 DP를 계산하기에 뒤에서부터
            DP[j] = max(DP[j], DP[j-W]+V)
# W부터 K까지, DP[j]의 현재 값 Vs DP[j-W]에 W를 추가하면 DP[j]가 되므로, DP[j-W]와 현재 V를 합친 값 갱신

print(max(DP))
