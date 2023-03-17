# 바이러스
# 결국 연결된 컴퓨터까지는 바이러스 감염됨

N = int(input())
R = int(input())
arr = [[] for _ in range(N+1)]

for i in range(R) :
    a, b = map(int,input().split())
    arr[a].append(b)
    arr[b].append(a)

Q = [1]
v = [1]

while Q :
    now = Q.pop(0)
    to = arr[now]
    for i in to :
        if i not in v :
            v.append(i)
            Q.append(i)

print(len(v)-1) # 1번 컴퓨터는 뺀 값이 결과값