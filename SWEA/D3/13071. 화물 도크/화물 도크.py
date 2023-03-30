# 화물 도크
# 화물차 사용 신청. 앞 작업이 종료돼야 뒷 작업이 가능함. 최대 몇 대가 이용 가능?

T = int(input())

for case in range(1, T+1) :
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    arr.sort(key = lambda x : (x[1], x[0]))     # 종료시간이 1순위, 그 뒤 시작시간을 2순위 기준으로 정렬
    ans = 0
    time = 0

    for i in arr :
        if i[0] >= time :       # 시작 시간이 현재 시간보다 크거나 같다면 사용신청 수리
            ans += 1
            time = i[1]

    print(f'#{case} {ans}')