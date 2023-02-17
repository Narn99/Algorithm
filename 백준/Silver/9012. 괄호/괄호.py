# 괄호
import sys

T = int(sys.stdin.readline().rstrip())

for data in range(1, T+1) :
    stk = []
    st = input()
    ans = 'YES'

    for ch in st :
        if ch == '(' :
            stk.append(ch)
        else :
            try :
                stk.pop()
            except :
                ans = 'NO'
                break
    if stk :
        ans = 'NO'
    print(ans)