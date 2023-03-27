# 에디터
# L은 왼쪽으로 1칸, D는 오른쪽으로 1칸, B는 왼쪽 문자 삭제, P $는 $라는 문자를 왼쪽에 추가
# 커서 초기 위치는 맨 뒤
# 커서 위치를 스택과 아웃으로 표현. 커서는 스택에 들어있는 마지막 글자의 뒤에 위치한 것.
# 즉 커서 왼쪽에서 벌어지는 일은 스택의 마지막 글자에다 처리하면 되는거고,
# 커서 오른쪽에서 벌어지는 일은 아웃의 첫 글자에다 처리하면 되는 것.

import sys
from collections import deque

stk = deque(list(sys.stdin.readline().rstrip()))
N = len(stk)
M = int(sys.stdin.readline())
out = deque()

for _ in range(M) :
    lst = list(sys.stdin.readline().split())
    if len(lst) == 2 :
        stk.append(lst[1])      # 받은게 길이가 2라는건 P '?'로 문자 넣으라는 뜻
    else :
        if lst[0] == 'L' :
            if stk :                # 받은게 L이고, 스택이 비어있지 않으면
                out.appendleft(stk.pop())   # 스택에서 뽑아서 아웃의 왼쪽에 추가
        elif lst[0] == 'D' :
            if out :                # 받은게 D이고, 아웃이 비어있지 않으면
                stk.append(out.popleft())   # 아웃의 왼쪽에서 뽑아서 스택에 추가
        else :
            if stk :                # 받은게 B이고, 스택이 비어있지 않으면
                stk.pop()           # 스택에서 뽑아서 그대로 버림

ans = ''.join(stk) + ''.join(out)   # 마지막으로 스택과 아웃을 합침.

print(ans)


