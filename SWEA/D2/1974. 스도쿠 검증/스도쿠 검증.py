# 스도쿠 검증 ~ 9x9 표에 행, 열, 3x3 칸에 1부터 9까지 숫자가 겹치지 않게
# 9x9 스도쿠 퍼즐 입력받으면, 행, 열, 3x3칸씩 탐색해서 겹치는 숫자가 없다면 1, 아니면 0 출력
# 행과 열 탐색은 함수로 만들어서 전치행렬 list(zip(*행렬))
 
T = int(input())
 
def check(lst) :        # 행과 열 검사, 중간에 전치행렬로 바꿔서 2번 검사
    for test in range(2) :
        for i in range(9) :
            check = set()
            for j in range(9) :   # 1~9까지 하나씩 들어가는거니 세트에 넣으면 길이가 9 돼야함
                check.add(lst[i][j])
            if len(check) != 9 :
                return 0
        lst = list(zip(*lst))    # 전치행렬
    return 1
 
def check_square(lst) :     # 작은 사각형 9칸 검사, 마찬가지로 세트의 길이가 9개인지 검사
    for i in range(3):
        for j in range(3):  # 여기까지가 큰 사각형 9개
            squ = set()
            for k in range(3 * i, 3 * (i + 1)):
                for l in range(3 * j, 3 * (j + 1)):  # 그 안의 작은 사각형 9개
                    squ.add(lst[k][l])
            if len(squ) != 9:
                return 0
    return 1
 
for case in range(T) :
 
    sudoku = []
    for i in range(9) :
        sudoku += [list(map(int,input().split()))]
 
    ans = check(sudoku)      # 행과 열 검사
 
    if ans == 1 :           # 행과 열 검사를 통과했다면, 3x3 검사
        ans = check_square(sudoku)
        print(f'#{case+1} {ans}')
    else :                  # 행과 열 검사 통과 못 했으면 그냥 0
        print(f'#{case+1} 0')