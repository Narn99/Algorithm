# 계산기 2
# 문자열로 이루어진 계산식, 후위 표기식으로 바꾸어 계산

dic = {'+' : 1, '*' : 2}
T = 10

for case in range(1, T+1) :

    N = int(input())
    st = input()
    stk = []
    calc = ''
    ans = 0
    
    # 후위 표기식으로 만들어보기
    for i in range(N) :
        try :
            int_check = int(st[i])  # 정수형이 가능하면 calc에 넣어줌. (정수 말고 문자열로)
            calc += st[i]
        except :
            if stk == [] :
                stk.append(st[i])   # 스택이 비어있다면 넣어줌
            else :
                if dic[st[i]] > dic[stk[-1]] :  # st[i]가 +, *일 때 중에서 우선순위에 따라 append 혹은 pop
                    stk.append(st[i])
                else :
                    while True :
                        if stk == [] or dic[stk[-1]] < dic[st[i]] :  # 스택 안이 더 높거나 같으면 pop 해주다가
                            stk.append(st[i])       # 스택이 비거나, 스택 안의 우선순위가 더 낮아지면 append하고 종료
                            break
                        calc += stk.pop()
    else :
        for _ in range(len(stk)) :
            calc += stk.pop()           # 스택 비우기

    # 이제 계산하기
    for i in range(N) :
        try :
            int_calc = int(calc[i])
            stk += [int_calc]           # 비운 스택 재활용으로 이번엔 숫자 넣어주기
        except :
            if calc[i] == '+' :
                a = stk.pop()           # +면 두개 뽑아서 합하고 넣어주기
                b = stk.pop()
                stk.append(b+a)
            elif calc[i] == '*' :
                a = stk.pop()           # *면 두개 뽑아서 곱하고 넣어주기
                b = stk.pop()
                stk.append(b*a)
    else :
        if len(stk) == 1 :              # 스택이 하나라면 ans에 그 값을 넣고 출력
            ans = stk[0]

    print(f'#{case} {ans}')