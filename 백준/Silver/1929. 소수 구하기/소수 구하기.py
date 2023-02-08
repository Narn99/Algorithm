def prime_list(n) :                     # 에라토스테네스의 체
    sieve = [True] * n                  # 2부터 소수를 구하면, 전체 범위에서 그 배수들을 다 제거하는 방식

    m = int(n**0.5)
    for i in range(2, m+1) :
        if sieve[i] :
            for j in range(i+i, n, i) :
                sieve[j] = False

    return [i for i in range(2, n) if sieve[i] == True]

M, N = map(int,input().split())

if N == 1 :
    pass
else :
    ans = prime_list(N+1)
    for i in ans :
        if i >= M :
            print(i)