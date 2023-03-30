# 수영장
# 가장 적은 비용으로 1년치 수영장 이용 계획 짜기, 백트래킹 최소값 구하기
# 1년치는 한 번이니까 따로 그냥 빼서 마지막에 비교하자

def dfs(n, sm) :
    global ans
    if sm > ans : return
    if n >= 12 :
        if sm < ans :
            ans = sm
        return
    else :
        days = go_to[n]
        dfs(n+1, sm + days*price[0])    # 일별 요금, 월별 요금, 3달별 요금 계산
        dfs(n+1, sm + price[1])
        dfs(n+3, sm + price[2])

T = int(input())

for case in range(1, T+1) :

    price = list(map(int, input().split()))
    go_to = list(map(int, input().split()))

    ans = 36000

    dfs(0, 0)

    if ans > price[3] :         # 1년치 가격이랑 현재 ans랑 비교
        print(f'#{case} {price[3]}')
    else :
        print(f'#{case} {ans}')