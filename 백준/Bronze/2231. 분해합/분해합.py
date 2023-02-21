# 분해합

import sys

N = int(sys.stdin.readline().rstrip())

for i in range(N) :
    ilst = list(map(int,list(str(i))))
    if sum(ilst) + i == N :
        ans = i
        break
else :
    ans = 0

print(ans)

