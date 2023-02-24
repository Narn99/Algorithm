# 직사각형을 만드는 방법
# n개의 정사각형으로 만들 수 있는 직사각형의 개수 => i * j로 다 쓸 수 있어야됨. => 약수들
# 근데 n개 다 안 쓰고도 만들 수 있으니, 1 ~ n개까지로 만드는 듯.
# 회전시켜서 같은건 미포함이니, i*j로 만들면 j*i는 포함 안 하는 것 => 약수의 개수 나누기 2 (정사각형 있는건 예외)

N = int(input())

ans = 0

for n in range(1, N+1) :        # n은 N보다 작거나 같은 정사각형 개수
    meas = []
    for i in range(1, n+1) :
        if n % i == 0 :
            meas.append(i)

    if len(meas) % 2 == 1 :     # 약수의 개수가 홀수면 정사각형 있는거니 +1
        ans += len(meas)//2 + 1
    else :
        ans += len(meas)//2

print(ans)