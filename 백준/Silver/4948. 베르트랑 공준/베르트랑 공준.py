# 베르트랑 공준
# 자연수 n에 대해, n보다 크고 2n보다 작거나 같은 소수는 적어도 하나 존재한다.

def prime_lst(n) :          # 에라토스테네스의 체
    num = [True] * n

    m = int(n**0.5)
    for i in range(2, m+1) :
        if num[i] :
            for j in range(i+i, n, i) :
                num[j] = False

    return [i for i in range(2,n) if num[i] == True]

while True :
    case = int(input())
    if case == 0 :              # 0이 입력되면 정지
        break
    else :
        ans = 0                         # 에라토스테네스의 체로 2*case+1까지 소수를 구한다
        prlst = prime_lst(2*case+1)     # (2n보다 작거나 같은거니 2n도 포함하도록 +1 해준 것)
        for i in prlst :
            if i > case :               # 그 중 case보다 큰 수 하나당 ans에 1 추가
                ans += 1
        print(ans)
