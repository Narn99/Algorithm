# 진기의 최고급 붕어빵
# N명의 사람이 각자의 시간에 도착하고, 붕어빵은 M초의 시간에 K개가 만들어짐
# 재고 붕어빵은 시간이 M이 될 때마다 K개씩 늘어나고,
# 그 재고는 사람이 도착할 때마다 감소해서 음수가 되지 않으면 가능, 음수가 되면 불가능
 
T = int(input())
 
for case in range(1, T+1) :
 
    N, M, K = map(int, input().split())
    lst = list(map(int,input().split()))
    time = fish = cnt = 0    # 시간, 붕어빵 재고, 도착한 사람 수
    ans = 'Possible'
 
    while True :
        if cnt == N : break     # 손님이 모두 도착했으면 종료
        if time % M == 0 and time > 0 : fish += K   # M초마다 K개 생산
        if time in lst :
            for person in lst :
                if person == time :    # 해당 시간에 도착한 손님마다 재고 1개 감소
                    cnt += 1
                    fish -= 1
        if fish < 0 :               # 만약 붕어빵 재고가 부족하면 ans 바꾸고 종료
            ans = 'Impossible'
            break
        time += 1
 
    print(f'#{case} {ans}')