# 줄 세우기

T = int(input())

for case in range(1, T+1) :

    lst = list(map(int,input().split()))
    tc = lst.pop(0)
    cnt = 0

    while True :
        if lst == sorted(lst) :
            break
        line = []
        for person in lst :
            if not line :       # 줄이 비어있으면 그냥 세움
                line.append(person)
            else :
                if max(line + [person]) == person : # 맨 뒤에 세우는 사람이 가장 크면 ok
                    line.append(person)
                else :        # 가장 큰게 아니면 가장 앞의 자기보다 큰 사람의 자리에 넣어줌
                    for bigger in range(len(line)) :
                        if line[bigger] > person :
                            cnt += len(line) - bigger   # 뒤로 가는 사람수만큼 카운팅 (걸음수)
                            line.insert(bigger, person)
                            break
        lst = line  # 리스트와 라인 동일화

    print(f'{tc} {cnt}')