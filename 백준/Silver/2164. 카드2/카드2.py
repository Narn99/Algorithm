# 카드 2 ~ deque

import sys
from collections import deque

N = int(sys.stdin.readline().rstrip())
lst = deque([i for i in range(1, N+1)])
idx = 0

while len(lst) > 1 :
    deque.popleft(lst)
    deque.append(lst, deque.popleft(lst))

print(lst[0])