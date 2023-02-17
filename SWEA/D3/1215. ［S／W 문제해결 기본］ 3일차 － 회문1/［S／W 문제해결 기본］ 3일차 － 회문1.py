# 회문1 ~ 기러기, 토마토처럼 앞뒤가 똑같은 문장이나 낱말이 회문
# 8x8 평면 글자판에서 제시된 길이의 회문 개수 구하기 (가로 혹은 세로만)
# 가로로 찾아본 뒤, 전치행렬로 바꾸고 가로가 된 세로를 찾기.
 
T = 10
 
def check(width, lst) :     # 길이와 글자판을 받는다
    cnt = 0
    for test in range(2) :     # 전치행렬로 2번 돌리기
        for i in range(8) :
            for j in range(8-width+1) :
                sl = lst[i][j:j+width]      # 각 행마다 width개씩 잘라서 회문인지 비교
                for k in range(width//2) :
                    if sl[k] != sl[-k-1] :
                        break           # 아니었다면 탈출
                else :                 # 회문이었다면 cnt에 1 추가
                    cnt += 1
        lst = list(zip(*lst))
    return cnt
 
for case in range(T) :
 
    N = int(input())
    wordlst = [list(input()) for _ in range(8)]
 
    ans = check(N, wordlst)
 
    print(f'#{case+1} {ans}')