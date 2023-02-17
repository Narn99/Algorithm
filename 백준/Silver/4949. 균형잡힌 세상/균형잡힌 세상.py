# 균형잡힌 세상
import sys

while True :
    st = sys.stdin.readline().rstrip()
    if st == '.' :
        break
    stk = []
    ans = 'no'

    for ch in st :
        if ch == ')' :
            if not stk or stk[-1] != '(':
                break
            else :
                stk.pop()
        elif ch == ']' :
            if not stk or stk[-1] != '[':
                break
            else:
                stk.pop()
        elif ch == '(' or ch == '[' :
            stk.append(ch)
    else :
        if not stk :
            ans = 'yes'

    print(ans)