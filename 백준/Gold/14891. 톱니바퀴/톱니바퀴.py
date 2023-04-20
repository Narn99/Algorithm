# 톱니바퀴
# 맞닿은 극이 같다면 움직이지 않고, 다르다면 반대 방향으로 움직임.
# 인덱스가 +가 되냐 -가 되냐인 듯
# 12시를 idx로 기록하고, +2, -2한 인덱스들이 좌, 우인거
# 톱니가 4개뿐이니 그냥 if 문으로 다 작성보기

import sys

gears = [0]     # 1~4번 톱니바퀴
for _ in range(4) :
    gears.append(sys.stdin.readline().rstrip())
idx = [0, 0, 0, 0, 0]   # 톱니바퀴 12시에 있는 극을 나타내는 인덱스


K = int(sys.stdin.readline())
for _ in range(K) :
    gear, dr = map(int, sys.stdin.readline().split())
    if dr == 1 :
        # 방향이 시계방향일 때, 양쪽 순번 톱니바퀴를 확인
        m_gear, p_gear = gear-1, gear+1
        # 각각 맞닿은 부분이 다른지 확인하고, 다르다면 다음 톱니바퀴와도 다른지 확인 진행
        # 전부 확인한 뒤에 인덱스를 옮겨준다.
        if 0 < m_gear < 5 and gears[m_gear][(idx[m_gear]+2)%8] != gears[gear][(idx[gear]-2)%8] :
            if 0 < m_gear-1 < 5 and gears[m_gear-1][(idx[m_gear-1]+2)%8] != gears[m_gear][(idx[m_gear]-2)%8] :
                if 0 < m_gear-2 < 5 and gears[m_gear-2][(idx[m_gear-2]+2)%8] != gears[m_gear-1][(idx[m_gear-1]-2)%8] :
                    idx[m_gear-2] = (idx[m_gear-2]+1)%8
                idx[m_gear-1] = (idx[m_gear-1]-1)%8
            idx[m_gear] = (idx[m_gear]+1)%8
        if 0 < p_gear < 5 and gears[p_gear][(idx[p_gear]-2)%8] != gears[gear][(idx[gear]+2)%8] :
            if 0 < p_gear+1 < 5 and gears[p_gear+1][(idx[p_gear+1]-2)%8] != gears[p_gear][(idx[p_gear]+2)%8] :
                if 0 < p_gear+2 < 5 and gears[p_gear+2][(idx[p_gear+2]-2)%8] != gears[p_gear+1][(idx[p_gear+1]+2)%8] :
                    idx[p_gear+2] = (idx[p_gear+2]+1)%8
                idx[p_gear+1] = (idx[p_gear+1]-1)%8
            idx[p_gear] = (idx[p_gear]+1)%8
        idx[gear] = (idx[gear] - 1) % 8

    else :
        # 방향이 반시계 방향일 때,
        m_gear, p_gear = gear-1, gear+1
        if 0 < m_gear < 5 and gears[m_gear][(idx[m_gear]+2)%8] != gears[gear][(idx[gear]-2)%8] :
            if 0 < m_gear-1 < 5 and gears[m_gear-1][(idx[m_gear-1]+2)%8] != gears[m_gear][(idx[m_gear]-2)%8] :
                if 0 < m_gear-2 < 5 and gears[m_gear-2][(idx[m_gear-2]+2)%8] != gears[m_gear-1][(idx[m_gear-1]-2)%8] :
                    idx[m_gear-2] = (idx[m_gear-2]-1)%8
                idx[m_gear-1] = (idx[m_gear-1]+1)%8
            idx[m_gear] = (idx[m_gear]-1)%8
        if 0 < p_gear < 5 and gears[p_gear][(idx[p_gear]-2)%8] != gears[gear][(idx[gear]+2)%8] :
            if 0 < p_gear+1 < 5 and gears[p_gear+1][(idx[p_gear+1]-2)%8] != gears[p_gear][(idx[p_gear]+2)%8] :
                if 0 < p_gear+2 < 5 and gears[p_gear+2][(idx[p_gear+2]-2)%8] != gears[p_gear+1][(idx[p_gear+1]+2)%8] :
                    idx[p_gear+2] = (idx[p_gear+2]-1)%8
                idx[p_gear+1] = (idx[p_gear+1]+1)%8
            idx[p_gear] = (idx[p_gear]-1)%8
        idx[gear] = (idx[gear] + 1) % 8

ans = 0
for i in range(1, 5):
    if gears[i][idx[i]] == '1' :
        ans += 2**(i-1)

print(ans)

