# 리모컨

import sys

N = int(sys.stdin.readline().rstrip())
M = int(sys.stdin.readline())
button = []

ans = abs(N - 100)

if M :
    broken = sys.stdin.readline().split()
else :
    broken = []

for num in range(1000001) :
    for n in str(num) :
        if n in broken :
            break
    else :
        ans = min(ans, len(str(num)) + abs(num - N))

print(ans)