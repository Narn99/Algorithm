# DFS, BFS

def DFS() :
    stk = [V]
    v = [0]*(N+1)
    route = []
    while stk :
        now = stk.pop()
        if v[now] == 0 :
            v[now] = 1
            route.append(now)
            for num in sorted(arr[now],reverse=True) :
                if v[num] == 0 :
                    stk.append(num)
    return route

def BFS() :
    stk = [V]
    v = [0]*(N+1)
    v[V] = 1
    route = []
    while stk :
        now = stk.pop(0)
        route.append(now)
        for num in sorted(arr[now]) :
            if v[num] == 0 :
                v[num] = 1
                stk.append(num)
    return route

N, M, V = map(int,input().split())
arr = [[]*(N+1) for _ in range(N+1)]
for _ in range(M) :
    a, b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)

D_ans = DFS()
B_ans = BFS()

print(*D_ans)
print(*B_ans)