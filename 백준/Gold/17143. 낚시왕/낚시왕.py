# 낚시왕 ~ 시뮬레이션
# 매 턴마다 낚시왕이 있는 열의 가장 위에 있는 상어는 죽음
# 이동방향으로 속도만큼 이동하며, 같은 칸에서 만나면 큰 상어한테 흡수당함
# 매 턴마다 상어들 이동시켜준 뒤, 내림차순 정렬로 같은 칸에 있는건 제일 큰거에 삭제

import sys

dic = {1: 2, 2: 1, 3: 4, 4: 3}

di = [0, -1, 1, 0, 0]
dj = [0, 0, 0, 1, -1]

R, C, M = map(int, sys.stdin.readline().split())
sharks = []
for _ in range(M):
    r, c, s, d, z = map(int, sys.stdin.readline().split())
    sharks.append([r - 1, c - 1, s, d, z])
ans = 0

for fishing_king in range(C):

    sharks.sort(key=lambda x: (x[1], x[0]))  # 낚시왕의 사냥 턴
    for num in range(len(sharks)):
        if sharks[num][1] == fishing_king:
            ans += sharks[num][4]
            shark = sharks[num]
            sharks.pop(num)
            break

    for n in range(len(sharks)):  # 상어 이동 턴

        if sharks[n][3] == 1:
            m = sharks[n][0] - (sharks[n][2] % (2 * (R - 1)))
            if m < 0:
                m = abs(m)
                if m > R-1 :
                    m = 2*(R-1)-m
                else :
                    sharks[n][3] = dic[sharks[n][3]]
            sharks[n][0] = m

        elif sharks[n][3] == 2:
            m = sharks[n][0] + (sharks[n][2] % (2 * (R - 1)))
            if m > R - 1:
                m = 2*(R-1)-m
                sharks[n][3] = dic[sharks[n][3]]
                if m < 0 :
                    m = abs(m)
                    sharks[n][3] = dic[sharks[n][3]]
            sharks[n][0] = m

        elif sharks[n][3] == 3:
            m = sharks[n][1] + (sharks[n][2] % (2 * (C - 1)))
            if m > C - 1:
                m = 2*(C-1)-m
                sharks[n][3] = dic[sharks[n][3]]
                if m < 0 :
                    m = abs(m)
                    sharks[n][3] = dic[sharks[n][3]]
            sharks[n][1] = m

        else:
            m = sharks[n][1] - (sharks[n][2] % (2 * (C - 1)))
            if m < 0:
                m = abs(m)
                if m > C-1 :
                    m = 2*(C-1)-m
                else :
                    sharks[n][3] = dic[sharks[n][3]]
            sharks[n][1] = m

    else:
        sharks.sort(key=lambda x: (x[0], x[1], x[4]))

    i = 1
    while i < len(sharks):
        if sharks[i][0] == sharks[i - 1][0] and sharks[i][1] == sharks[i - 1][1]:
            sharks.pop(i - 1)
            continue
        i += 1

else:
    print(ans)

