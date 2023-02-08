# 설탕 배달
# 설탕 N 킬로그램 배달, 봉지는 3인가 5킬로그램
# 최소한의 봉지 수로 배달할 것
# 정확하게 N킬로그램 배달해야함. 실패하면 -1 출력
# N을 5로 나눈 나머지가 3이면, 5로 나눈 몫 + 1, 나머지가 0이면 걍 5로 나눈 몫
# 그 외에는 N을 5로 나눈 몫부터 -1씩 해가는 i로 N-(5*i)가 3으로 나누어지는지 check

N = int(input())

big, small = 0, 0

if N % 5 == 3 :
    big, small = N//5 , 1
elif N % 5 == 0 :
    big, small = N//5 , 0
else :
    for i in range(N//5, -1, -1) :
        remain = N - 5*i
        if remain % 3 == 0 :
            big = i
            small = remain // 3
            break      # 5짜리 봉투가 많은 것부터 찾으니까, 결과 나오면 더 낮은데서 갱신 안 되게 바로 종료시킨다

if (big, small) == (0, 0) :
    print(-1)
else :
    print(big+small)
