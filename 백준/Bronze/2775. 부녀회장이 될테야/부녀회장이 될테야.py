T = int(input())

for case in range(T) :

    k = int(input())
    n = int(input())
    cnt = [[i for i in range(1, n+1)]]  # 0층의 n호까지 기본 입력, 층마다 구할 check 리스트를 더해줄 것

    for i in range(1, k+1) :    # 0층부터 있으니까, 1부터 k까지 탐색
        check = [1]             # 매 층마다 1호실은 1명, 매 층 인원을 넣어줄 리스트
        for j in range(1, n) :
            check += [check[j-1] + cnt[i-1][j]]     # 현재 방 좌표의 왼쪽 방과 아랫쪽 방의 합이 현재 방 인원
        cnt += [check]

    print(cnt[k][n-1])