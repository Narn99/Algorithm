# 수 정렬하기

N = int(input())
Nlst = []

for i in range(N) :
    Nlst += [int(input())]

Nlst = sorted(Nlst)

for i in range(N) :
    print(Nlst[i])