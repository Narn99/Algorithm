# 주사위 윷놀이
# 외곽 라인은 점수가 위치*2, 5번째 해당하는 라인에 도착하면 무조건 안쪽 라인 타야됨.
# 말이 4개니까, 말 각각이 어디에 있는지 값으로 기록하며 하기?
# 말고.... 0~42까지 있는 배열을 만들고, 점수칸대로 배열에? 백트래킹?

###### 22, 24, 26, 28, 30 이 다섯개는 다른 길에도 점수가 있네!!!!!

import sys
from copy import deepcopy

road = [[i*2 for i in range(21)]
,[10, 13, 16, 19, 25, 30, 35, 40]
,[20, 22, 24, 25, 30, 35, 40]
,[30, 28, 27, 26, 25, 30, 35, 40]]

def check(n, sm, pieces) :
    global score

    if n == 10 :
        if sm > score :
            score = sm
        return

    dice = dices[n]

    for num in range(4) :
        piece = pieces[num][0]
        route = pieces[num][1]
        if piece != -1 :
            temp = deepcopy(pieces)
            temp[num][0] += dice
            if route == 0 :
                if temp[num][0] == 5 :
                    temp[num][1] = 1
                    temp[num][0] = 0
                elif temp[num][0] == 10 :
                    temp[num][1] = 2
                    temp[num][0] = 0
                elif temp[num][0] == 15 :
                    temp[num][1] = 3
                    temp[num][0] = 0

            # 인덱스 넘어가는건 = 도착점에 도달한 것
            if temp[num][0] >= len(road[temp[num][1]]) :
                temp[num][0] = -1
                check(n+1, sm, temp)
            else :
                num_score = road[temp[num][1]][temp[num][0]]
                for i in range(4) :
                    # 마지막 도착점에 도달해있는건 중복 확인 안 해도 되므로 continue
                    if temp[i][0] == -1 :
                        continue
                    if i != num :
                        i_score = road[temp[i][1]][temp[i][0]]
                        if num_score == i_score :
                            if num_score == 30 :
                                # 30일 때는 루트 3의 다른 위치에 30이 따로 있기 때문에,
                                # 루트랑 인덱스 비교를 다 해줘야 함.
                                # 특히 둘 다 3루트라면, 값이 30이어도 위치가 다를 수 있음. 인덱스 비교
                                if temp[num][1] == 3 and temp[i][1] == 3 :
                                    if temp[num][0] == temp[i][0] :
                                        break
                                elif temp[num][1] == 3 :
                                    if temp[num][0] == 5 :
                                        break
                                elif temp[i][1] == 3 :
                                    if temp[i][0] == 5 :
                                        break
                                else :
                                    break
                            # 점수도 같고, 루트도 같으면 그냥 같은 위치
                            elif temp[i][1] == temp[num][1] :
                                break
                            # 25, 35, 40은 3루트에 다 있으니까, 1~3에선 루트 달라도 같은거
                            elif num_score in (25, 35, 40) :
                                break
                else :
                    check(n+1, sm+num_score, temp)


dices = list(map(int, sys.stdin.readline().split()))

score = 0
pieces = [[0]*2 for _ in range(4)]

check(0, 0, pieces)

print(score)
