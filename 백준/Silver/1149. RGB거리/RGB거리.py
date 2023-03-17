# RGB 거리
# 이전 집과 현재 집의 색은 달라야함. 비용 최솟값 찾기.
# 현재 집까지의 코스트는 이전 색이 다른 집들까지의 코스트 + 현재 집 코스트들 중 최솟값

N = int(input())
arr = [list(map(int,input().split())) for _ in range(N)]
cost = [[0, 0, 0] for _ in range(N)]
cost[0] = arr[0]

for i in range(1, N) :
    cost[i][0] = min(cost[i-1][1], cost[i-1][2]) + arr[i][0]
    cost[i][1] = min(cost[i-1][0], cost[i-1][2]) + arr[i][1]
    cost[i][2] = min(cost[i-1][0], cost[i-1][1]) + arr[i][2]

print(min(cost[-1]))