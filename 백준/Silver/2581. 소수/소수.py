# 소수
# M과 N을 주고, M과 N 사이의 자연수 중 소수를 모두 골라, 합과 최솟값을 구하기.

M = int(input())
N = int(input())
lst = [i for i in range(M, N+1)]    # M부터 N까지 다 넣은 리스트

for i in range(M, N+1) :
    if i == 1 :                     # 1은 소수 아니니 제거
        lst.remove(i)
        continue
    for j in range(2, i//2+1) :     
        if i % j == 0 :             # lst에서 소수 아닌건 다 제거
            lst.remove(i)
            break

if lst == [] :
    print(-1)
else :
    print(sum(lst))
    print(min(lst))