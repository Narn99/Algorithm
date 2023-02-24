# 홈 방범 서비스 ~ 마름모 공간만 제공하는 서비스, 영역 크기만큼 비용이 들어간다.
# 운영비용 = K*K + (K-1)*(K-1), 정사각형 범위에서 벗어나도 운영비용에 포함됨
# 범위 K라는건 중앙 포함으로 1개부터 세서, K번까지 이동할 수 있는 범위.
# 4방향 말고 범위 탐색으로 해보자. (4방향은 너무 오래 걸려서 시간초과)

def check(i, j, K) :
    global house
    visit = [[0]*N for _ in range(N)]    # K 범위 안에 1이 있는지, 있다면 visit에 넣어주며 체크
    for k in range(K) :
        for l in range(K-k) :
            if 0 <= i+k < N and 0 <= j+l < N :     # 우하향 방면
                if city[i+k][j+l] == 1 and visit[i+k][j+l] == 0 :
                    visit[i+k][j+l] = 1
                    house += 1
            if 0 <= i+k < N and 0 <= j-l < N :     # 좌하향 방면
                if city[i+k][j-l] == 1 and visit[i+k][j-l] == 0 :
                    visit[i+k][j-l] = 1
                    house += 1
            if 0 <= i-k < N and 0 <= j+l < N :     # 우상향 방면
                if city[i-k][j+l] == 1 and visit[i-k][j+l] == 0 :
                    visit[i-k][j+l] = 1
                    house += 1
            if 0 <= i-k < N and 0 <= j-l < N :     # 좌상향 방면
                if city[i-k][j-l] == 1 and visit[i-k][j-l] == 0 :
                    visit[i-k][j-l] = 1
                    house += 1
    return

T = int(input())

for case in range(1, T+1) :

    N, M = map(int,input().split())
    city = [list(map(int,input().split())) for _ in range(N)]
    mx_house = 0
    K = 1
    mx_pf = 0
    house_in_city = 0
    for i in range(N) :
        for j in range(N) :
            if city[i][j] == 1 :
                mx_pf += M          # 해당 도시 최대 지불 가능값
                house_in_city += 1  # 해당 도시에 있는 전체 집

    while True :
        cost = K ** 2 + (K - 1) ** 2
        if cost > mx_pf :   # 코스트가 최대 지불값을 넘으면 종료
            break
        for i in range(N) :
            for j in range(N) :
                house = 0
                check(i, j, K)
                if house > mx_house and house*M >= cost :
                    mx_house = house
        if mx_house == house_in_city :  # 서비스 제공받을 집 최대수가 도시 전체 집과 같아지면 종료
            break
        K += 1

    print(f'#{case} {mx_house}')