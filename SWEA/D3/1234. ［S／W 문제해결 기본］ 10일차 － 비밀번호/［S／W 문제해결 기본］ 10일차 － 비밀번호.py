# 비밀번호
# stack -> password에 하나 하나 넣어가며, top에 있는게 현재랑 같다면 둘 같이 소거시키기.
# 전부 입력했고, 더이상 소거가 불가능한게 비밀번호

T = 10

for case in range(1,T+1) :

    N, M = input().split()
    long = int(N)
    numbers = list(M)
    password = []
    top = -1

    for num in numbers :
        if top >= 0 and num == password[top] :
            password.pop()
            top -= 1        # password에 입력된 마지막 것과 num이 같다면 둘 다 빠진다.
        else :
            password += [num]
            top += 1        # 아니라면 password에 새로 추가.

    ans = ''.join(password)

    print(f'#{case} {ans}')