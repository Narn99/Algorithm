# 골드바흐의 추측 ~ 2보다 큰 짝수는 모두 두 소수의 합으로 나타낼 수 있다는 추측

def is_prime(n) :    # 소수인지 확인
    if n == 1 :
        return False
    else :
        for i in range(2, int(n**0.5)+1) :
            if n % i == 0 :
                return False
        return True

T = int(input())

for case in range(T) :

    n = int(input())
                        # n의 중간부터 양 끝으로 향해 가면서, 합쳐서 n이 되는 두 소수가 있으면 찾고 바로 종료. (중간부터 찾으니까)
    for i in range(n//2, 1, -1) :
        if is_prime(i) and is_prime(n-i) :
            print(i, n-i)
            break