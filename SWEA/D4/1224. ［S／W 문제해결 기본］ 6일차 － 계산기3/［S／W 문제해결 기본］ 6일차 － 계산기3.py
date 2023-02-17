# 계산기3
# +, * 연산자, 피연산자는 0~9, 괄호가 존재함

in_stk = {'(' : 0, '+' : 1, '*' : 2}
out_stk = {'(' : 3, '+' : 1, '*' : 2}

T = 10

for case in range(1, T+1) :

    N = int(input())
    st = input()
    calc_st = ''
    stk = []
    ans = 0
    cnt = 0

    for ch in st :
        try :
            a = int(ch)
            calc_st += ch
        except :
            if stk == [] :
                stk.append(ch)
            elif ch == ')' :    # )을 발견하면, (이 나올 때까지 pop
                while True :
                    if stk[-1] == '(' :
                        stk.pop()
                        break
                    else : calc_st += stk.pop()
            elif out_stk[ch] > in_stk[stk[-1]] :        # 밖이 더 크면 push
                stk.append(ch)
            elif out_stk[ch] == in_stk[stk[-1]] :       # 같다면 그냥 밖에 있는거 계산식에 표기
                calc_st += ch
            else :
                while True :    # 밖이 같거나 더 작으면 반복문을 돌린다
                    if out_stk[ch] == in_stk[stk[-1]] : # 밖과 안이 같아지면 밖을 계산식에 표기해주고 종료
                        calc_st += ch
                        break
                    elif out_stk[ch] > in_stk[stk[-1]] : # 밖이 더 커지면 push해주고 종료
                        stk.append(ch)
                        break
                    else :
                        calc_st += stk.pop()            # 그 외엔 밖이 작은 상태니 pop해줌
    else :
        for _ in range(len(stk)) :
            calc_st += stk.pop()        # 스택 비우기

    for ch in calc_st :
        try :
            a = int(ch)
            stk += [a]       # 어차피 빈 스택이니 재활용
        except :
            if ch == '+' :
                left = stk.pop()
                right = stk.pop()
                stk.append(left+right)
            else :
                left = stk.pop()
                right = stk.pop()
                stk.append(left*right)
    else :
        if len(stk) == 1 :
            ans = stk[0]

    print(f'#{case} {ans}')