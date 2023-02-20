# 스택 수열

import sys

n = int(sys.stdin.readline().rstrip())
stk = []
numbers = []
ans = []
cnt = 0

for _ in range(n) :
    numbers += [int(sys.stdin.readline().rstrip())]

for i in range(1, n+1) :
    stk.append(i)           # 일단 무조건 push
    ans += ['+']
    while True :
        if stk and stk[-1] == numbers[cnt] :
            stk.pop()
            cnt += 1        # 스택 최후미가 수열 현재 자리에 와야하면 pop
            ans += ['-']
        else :
            break

if stk :
    print('NO')      # 스택이 남아있으면 NO
else :
    for j in ans :
        print(j)