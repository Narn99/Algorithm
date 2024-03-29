# N-Queen
# N행 N열에 N개의 퀸을 놓는다면, 각 행, 각 열에 하나의 퀸만 존재해야함
# 방문한 행과 열을 기록해서 제외시키고, 나머지 중에서 대각선 탐색으로 다른게 없으면 두고 백트래킹?
import sys

def check(n, r, C, d1, d2) :
    global ans

    if n == N :     # n이 N과 같다는건, 조건 다 뚫고 놓은거니 그냥 ans에 1 추가
        ans += 1
        return

    for j in range(N) :     # 현재 행에서 사용 안 한 열에서, 대각선 체크하고 괜찮으면 둔다.
        if j not in C :
            if (r+j) not in d1 and (j-r) not in d2 :
                check(n+1, r+1, C+[j], d1 + [r+j], d2 + [j-r])

N = int(sys.stdin.readline())
d1 = []  # 대각선과 열 기록할 리스트
d2 = []
C = []
ans = 0

check(0, 0, C , d1, d2)

print(ans)