# 딱지놀이
# 1순위 별, 2순위 동그라미, 3순위 네모, 4순위 세모, 모두 같다면 무승부

N = int(input())

for case in range(1, N+1) :

    Alst = list(map(int,input().split()))
    a = Alst.pop(0)     # 첫 인덱스는 카드 개수
    Blst = list(map(int,input().split()))
    b = Blst.pop(0)     # 첫 인덱스는 카드 개수

    cntA = [0]*4
    cntB = [0]*4

    for shape in Alst :     # A 카드 문양 세기
        if shape == 4 : cntA[0] += 1
        elif shape == 3 : cntA[1] += 1
        elif shape == 2 : cntA[2] += 1
        else :            cntA[3] += 1

    for shape in Blst :     # B 카드 문양 세기
        if shape == 4 : cntB[0] += 1
        elif shape == 3 : cntB[1] += 1
        elif shape == 2 : cntB[2] += 1
        else :            cntB[3] += 1

    for i in range(4) :
        if cntA[i] > cntB[i] :   # A승
            print('A')
            break
        elif cntA[i] < cntB[i] : # B승
            print('B')
            break
    else :
        print('D')      # 다 돌도록 승패 안 났으면 무승부
