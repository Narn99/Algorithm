# 연결 요소의 개수
# 점 하나 잡고 BFS 돌려서 연결된거 전부 찾아 기록하고 그걸 연결요소 1개로 기록
# 그 뒤, 방문한 적 없는 점 하나 잡고 또 반복

import sys

N, M = map(int, sys.stdin.readline().split())
arr = [[] for _ in range(N+1)]

for _ in range(M) :
    a, b = map(int, sys.stdin.readline().split())
    arr[a].append(b)
    arr[b].append(a)

v = []
ans = 0

for num in range(1, N+1) :
    if num in v :
        continue
    else :
        Q = [num]
        while Q :
            now = Q.pop(0)
            to = arr[now]
            for i in to :
                if i not in v :
                    v.append(i)
                    Q.append(i)
        ans += 1

print(ans)