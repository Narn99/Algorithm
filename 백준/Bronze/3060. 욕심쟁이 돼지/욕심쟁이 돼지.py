# 욕심쟁이 돼지

T = int(input())

for case in range(1, T+1) :

    N = int(input())
    pigs = list(map(int, input().split()))
    day = 1

    while True :
        today = [0] * 6
        if sum(pigs) > N :   # 현재 사료값이 N보다 크면 종료
            break
        for i in range(6) :
            today[i] = pigs[i] + pigs[(i-1)%6] + pigs[(i+1)%6] + pigs[(i+3)%6]
        day += 1
        pigs = today

    print(day)