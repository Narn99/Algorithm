# 백만장자 프로젝트
# N일 동안의 매매가 예측, 하루 1만큼 구매, 판매는 언제든 가능.
# 현재 시점에서 N일 뒤까지 오르는 구간이 있으면 그 전날까지 사서, 그 날에 판다.
# N일 뒤까지 오르는게 보이지 않는다면 안 삼.
# 현재 위치부터 마지막 날까지의 최댓값이 뒤에 있다면 구매, 최댓값이 되는 날에 재고 전부 판매.
# 그 뒤에 또 오르는 구간이 있으면 사재기
# 시간초과.. 반복문 줄여보기.

def sajaegi(N) :
    n = 0
    profit = 0
    while True :
        if n >= N-1 :       # n이 마지막 요소에 도달하면 종료
            break
        else :
            mx = 0
            maxday = 0
            for i in range(n, N) :  # 현재 위치인 n보다 뒤에서 최대 가격과 그 일자를 찾음.
                if lst[i] > mx :
                    mx = lst[i]
                    maxday = i
            else :                      # 그 날의 가격 - 그 이전 날들의 가격들을 쭉 더해줌
                for j in range(n,maxday) :
                    profit += mx - lst[j]
                else :                  # 그 최대가격 날짜 이후로 넘김.
                    n = maxday + 1
    return profit

T = int(input())

for case in range(1, T+1) :

    N = int(input())
    lst = list(map(int,input().split()))
    ans = sajaegi(N)

    print(f'#{case} {ans}')
