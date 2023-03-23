# 최단경로
# BFS + 가중치(거리)
# 해당 정점까지의 최단거리를 기록하며 우선순위 큐 방식으로 품..
# 시간초과 메모리초과 엄청 난다.. 힙을 써야만 하는 듯.

import sys
import heapq
INF = 100000000         # 거리 시작은 일단 엄청 큰 수

V, E = map(int, sys.stdin.readline().split())
K = int(sys.stdin.readline())

arr = [[] for _ in range(V+1)]
dist = [INF]*(V+1)      # 거리 기록
dist[K] = 0             # 시작점은 거리 0

for i in range(E) :
    u, v, w = map(int, sys.stdin.readline().split())
    arr[u].append((v, w))       # 이동할 정점과 거리 기록

Q = []     # 큐에 우선 시작점 넣어줌
heapq.heappush(Q, (0, K))

while Q :
    dis_now, now = heapq.heappop(Q)     # 현재 위치한 정점
    if dis_now > dist[now] :   # 힙에서 꺼낸 이동거리가 기존 거리보다 크다면 넘김
        continue
    for node_info in arr[now] :
        node, node_dist = node_info[0], node_info[1]        # 이동 가능한 정점들
        to_dist = dist[now] + node_dist
        if to_dist < dist[node] :           # 이동해야되는 거리가 기존 거리보다 짧다면,
            dist[node] = to_dist
            heapq.heappush(Q, (to_dist, node))   # 정점까지의 거리를 기록하며, 힙에다가 넣어줌

for d in range(1, len(dist)) :
    if dist[d] == INF :         # 도달 못 하면 INF 출력
        print('INF')
    else :
        print(dist[d])         # 나머진 최단 거리 출력