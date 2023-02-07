# ACM 호텔

T = int(input())

for case in range(T) :

    H, W, N = map(int,input().split())

    hotel = [[0]*W for _ in range(H)]       # 가로 W X 세로 H인 호텔
    cnt = 0
    ans = 0


    for i in range(W) :
        for j in range(H) :                 # 엘리베이터가 좌측인데, 좌측에서 가깝고 아래층인 방부터 배분이라면,
            hotel[j][i] += 1                # 보통 배열을 왼쪽으로 90도 돌린 것과 마찬가지
            cnt += 1
            if cnt == N :                   # 왼쪽 아래부터 채워가며, cnt에 1을 더해 cnt == N이 되는 손님의 방번호
                ans += (j+1)*100 + (i+1)    # 즉 (j+1)*100 + (i+1)이 그 N번째 손님의 방 번호
                break
        if cnt == N :
            break

    print(ans)