# 파리퇴치3
# +나 x 형태로 분사되는 중심으로부터 m의 거리까지 파리 퇴치하는 스프레이.
# 좌표별 4방향의 두 종류로 탐색, 잡는 파리수의 최댓값을 갱신
 
di1 = [-1, 1, 0, 0]
dj1 = [0, 0, -1, 1]
di2 = [-1, -1, 1, 1]
dj2 = [-1, 1, -1, 1]
 
def check() :
    global ans
    for i in range(N) :
        for j in range(N) :
            sm1 = sm2 = arr[i][j]
            for k in range(4) :
                ci1, cj1 = ci2, cj2 = i, j  # 방향 탐색할 때마다 좌표와 이동거리 초기화
                cnt1 = cnt2 = 1
                while True :
                    ni1, nj1 = ci1+di1[k], cj1+dj1[k]   # + 방향 탐색하며 sm1에 더해줌
                    if 0 <= ni1 < N and 0 <= nj1 < N :
                        sm1 += arr[ni1][nj1]
                        cnt1 += 1
                        if cnt1 == M : break
                        ci1, cj1 = ni1, nj1
                    else : break
                while True :
                    ni2, nj2 = ci2 + di2[k], cj2 + dj2[k]   # x 방향 탐색하며 sm2에 더해줌
                    if 0 <= ni2 < N and 0 <= nj2 < N :
                        sm2 += arr[ni2][nj2]
                        cnt2 += 1
                        if cnt2 == M : break
                        ci2, cj2 = ni2, nj2
                    else : break
            if sm1 > ans : ans = sm1        # 최댓값 갱신
            if sm2 > ans : ans = sm2
    return
 
 
T = int(input())
 
for case in range(1, T+1) :
 
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    ans = 0
 
    check()
 
    print(f'#{case} {ans}')