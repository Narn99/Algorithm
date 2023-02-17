# 제로

import sys

K = int(sys.stdin.readline().rstrip())
stk = []
for _ in range(K) :
    num = int(sys.stdin.readline().rstrip())
    if num == 0 :
        stk.pop()
    else :
        stk.append(num)

print(sum(stk))