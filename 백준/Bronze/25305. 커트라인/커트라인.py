# 커트라인

N, k = map(int,input().split())
Nlst = list(map(int,input().split()))

Nlst.sort(reverse=True)

print(Nlst[k-1])