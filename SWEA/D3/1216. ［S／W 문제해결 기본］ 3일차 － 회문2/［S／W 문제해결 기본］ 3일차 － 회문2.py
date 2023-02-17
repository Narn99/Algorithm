# 회문2 ~ 앞뒤가 똑같은 전화번호 1577은 1577-1577이라 회문은 아님
# 가로세로 100인 글자판에서, 가로 세로 모두에서 가장 긴 회문 길이 구하기
# 긴 것에서부터 작은 순으로 구하고, 가로랑 세로에서 찾은거 비교하면 될 듯
 
def check(lst) :
    for i in range(100, 0, -1) :        # 길이 100부터 1까지 탐색 (답 발견하면 바로 탈출 가능)
        for garosero in range(2) :      # 매 길이마다 행렬을 전치행렬로 뒤집어가며 탐색
            for row in range(100) :
                for col in range(100-i+1) :
                    for sen_col in range(i) :       # 리스트 안 만들고 위치로 직접 비교
                        if lst[row][col+sen_col] != lst[row][col+i-sen_col-1] :
                            break
                    else :                              # 제대로 되면 그 i값 바로 반환
                        return i
            lst = list(zip(*lst))
    return False
 
T = 10
 
for case in range(T) :
 
    t = int(input())
    lst = [list(input()) for _ in range(100)]
    ans = check(lst)
    print(f'#{t} {ans}')