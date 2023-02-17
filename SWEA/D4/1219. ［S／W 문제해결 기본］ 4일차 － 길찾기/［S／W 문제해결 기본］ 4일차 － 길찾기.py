# 길찾기
# A는 0, B는 99로 일방통행인 길을 지나서 A에서 B까지 갈 수 있나 확인
 
T = 10
 
for case in range(1, T+1) :
 
    tc, N = map(int,input().split())
    arr = [[] for _ in range(100)]          # 이번엔 특정 인덱스에 갈 수 있는 길만 넣은 배열
    nums = list(map(int,input().split()))
    for i in range(N) :
        arr[nums[2*i]] += [nums[2*i+1]]     # 0부터 짝수는 배열의 인덱스, 홀수는 값으로
 
    now = 0
    ans = 0
    stk = []
    no_way = []
 
    while True :
        if now == 99 :       # 위치가 99에 도달하면 ans를 1로 바꾸고 종료
            ans = 1
            break
        else :
            for i in arr[now] :
                if i not in no_way :     # now에서 갈 수 있는 길이, no_way에 있는 길이 아니라면 가본다.
                    stk = [now]
                    now = i
                    break
            else :
                no_way += [now]         # 갈 수 있는 길이 없으면 no_way에 넣어주고, 이전 위치로 돌아감.
                try :
                    now = stk.pop()
                except :
                    break       # 만약 뽑아낼게 없는 빈 칸이면, while문 종료
 
    print(f'#{tc} {ans}')