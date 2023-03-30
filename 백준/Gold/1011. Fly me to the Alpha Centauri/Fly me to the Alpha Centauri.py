# Fly me to the Alpha Centauri
# 시작은 1, 마지막도 1로 두 지점 사이를 최소 횟수 이동하기
# 몇 번째 자리까지 몇 번만에 도착할 수 있는가의 규칙이 존재................
# 거리 1은 1번, 거리 2는 2번, 거리 3은 3번, 거리 4도 3번, 거리 5와 6은 4번, 7~9는 5번
# 1, 2, 3, 3, 4, 4, 5, 5, 5, 6, 6, 6, 7....

import sys

INF = int(1e8)

def check() :
    cnt = 0
    for i in range(1, INF) :   # 특정 거리까지 이동하는 횟수가 (i+1)//2개씩 반복됨
        cnt += (i+1)//2        # 즉 횟수는 1씩 증가한다 하면, i를 1씩 키우며 (i+1)//2를 합산하면 거리 추측 가능
        if dist <= cnt :       # 결과적으로 cnt보다 dist가 작게 되는 최초의 순간인 i, 그 dist까지 이동은 i가 최소 횟수라는 것.
            return i

T = int(sys.stdin.readline())

for case in range(1, T+1) :
    x, y = map(int, sys.stdin.readline().split())
    dist = y-x

    ans = check()

    print(ans)