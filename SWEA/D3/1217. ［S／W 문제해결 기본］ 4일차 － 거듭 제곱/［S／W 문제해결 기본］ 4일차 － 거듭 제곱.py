# 거듭 제곱

def zegop(N, M) :
    if M == 1 :     # M이 1이면 N을 반환
        return N
    else :          # 그 외엔 M에서 1을 빼가며 N을 곱해가는 재귀함수
        return N * zegop(N, M-1)

T = 10

for case in range(1, T+1) :

    t = int(input())
    N, M = map(int,input().split())

    print(f'#{case} {zegop(N,M)}')
