# 빙고
# 철수 빙고판에 MC가 부르는거 0으로 만들기.
# 어느정도 지나면 빙고 체크 시작

CS = [input().split() for _ in range(5)]
MC = []
for _ in range(5) :
    MC += input().split()

cnt = 0

for num in range(25) :
    for row in range(5) :
        if MC[num] in CS[row] :
            idx = CS[row].index(MC[num])
            CS[row][idx] = '0'
            cnt += 1
    if num > 10 :
        bingo = 0
        for row in range(5) :   # 행 빙고 체크
            if CS[row][0] == '0' and CS[row].count('0') == 5 :
                bingo += 1
        for col in range(5) :   # 열 빙고 체크
            if CS[0][col] == '0' :
                for row in range(5) :
                    if CS[row][col] != '0' :
                        break
                else :
                    bingo += 1
        for rd in range(5) :    # 우하향 대각선 체크
            if CS[rd][rd] != '0':
                break
        else :
            bingo += 1
        for ru in range(5) :    # 좌하향 대각선 체크
            if CS[4-ru][ru] != '0' :
                break
        else :
            bingo += 1
        if bingo >= 3 :
            break

print(cnt)