# 최소비용 구하기
# 힙써서 다익스트라로 풀기

import sys
import heapq
inp = sys.stdin.readline
INF = 100000000

N = int(inp())
M = int(inp())

arr = [[] for _ in range(N+1)]
cost = [INF]*(N+1)      # 비용 기록

for _ in range(M) :
    a, b, c = map(int, inp().split())
    arr[a].append((b, c))

start, end = map(int, inp().split())  # 출발점과 도착점

Q = []
cost[start] = 0     # 출발점은 비용 0으로 초기화
heapq.heappush(Q, (0, start))

while Q :
    now_cost, now = heapq.heappop(Q)
    if now_cost > cost[now] :   # 꺼낸 비용이 기존에 기록된 비용보다 비싸면 스킵
        continue
    else :
        for go_to in arr[now] :
            node, node_cost = go_to[0], go_to[1]
            to_cost = node_cost + cost[now]
            if to_cost < cost[node] :    # 갈 수 있는 도시 탐색하며, 가는데 드는 비용이 적으면 힙에 넣어줌.
                cost[node] = to_cost
                heapq.heappush(Q, (to_cost, node))

print(cost[end])