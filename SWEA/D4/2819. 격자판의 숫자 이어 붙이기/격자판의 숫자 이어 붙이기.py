# 격자판의 숫자 이어 붙이기
# 7개 이동하며 숫자를 찾는데, 이미 중복인건 저장?
# 완전탐색으로 찾으면서 중복체크를 위해 이미 센 수열은 v에다 저장해둔다.

di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]

def check(ci, cj, lst) :
    global ans

    if len(lst) == 7 :
        sm = int(''.join(lst))
        if sm not in v :    # 완성한 수가 v에 없으면 추가, 답에 1 추가
            v.append(sm)
            ans += 1
        return

    for k in range(4) :
        ni, nj = ci+di[k], cj+dj[k]     # 4방향 탐색 진행
        if 0<=ni<4 and 0<=nj<4 :
            check(ni, nj, lst+[arr[ni][nj]])

T = int(input())

for case in range(1, T+1) :

    arr = [input().split() for _ in range(4)]
    v = []
    ans = 0

    for i in range(4) :
        for j in range(4) :
            check(i, j, [arr[i][j]])

    print(f'#{case} {ans}')