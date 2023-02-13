# 통계학

from collections import Counter
import sys

N = int(sys.stdin.readline())
Nlst = []
for _ in range(N) :
    a = int(sys.stdin.readline())
    Nlst += [a]
Nlst.sort()

print(round(sum(Nlst)/N))

print(Nlst[N//2])

cnt = Counter(Nlst).most_common(2)

if N > 1 :
    if cnt[0][1] == cnt[1][1] :
        print(cnt[1][0])
    else:
        print(cnt[0][0])
else :
    print(cnt[0][0])

print(max(Nlst) - min(Nlst))