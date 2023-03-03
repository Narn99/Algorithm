# Magnetic
# 빨간건 1 아래로, 파란건 2 위로. 중간에 부딪히면 그 자리에 멈춰서 교착상태
# 교착상태의 개수 구하기.. 교착의 위치를 구하는게 아니라 개수 구하는거니까,
# 열 탐색으로 1을 찾으면, 그 밑에 2가 나올 때까지 탐색하고 끝까지 없으면 0 있으면 1을 답에 추가
# 여러개 겹쳐도 교착 상태는 1개이므로, 중간에 만나는 1은 무시한다.
# while문으로 열마다 행 순회하면서, 1을 만나면 2를 만날 때까지 쭉 스킵, 만나면 그 다음부터 탐색
# 100행까지 다 돌았으면 다음 열로 이동하고, 그렇게 100열까지 다 돌면 종료.
 
T = 10
 
for case in range(1, T+1) :
 
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(100)]
    ans = row = col = 0
    now = 'S'
 
    while True :
        if row == 100 and col == 99 :   # 끝까지 다 돌았으면 종료
            break
        if row == 100 :         # 행의 끝에 도달했으면 다음 열로
            col += 1
            now = 'S'           # 자성체도 초기화
            row = 0
        if now == 'N' and arr[row][col] == 2 :  # 지금 N이고, 2를 만나면 답에 1 추가하고 S로 변경
            ans += 1
            now = 'S'
        elif now != 'N' and arr[row][col] == 1 : # 지금 N이 아닌데, 1을 만나면 N으로 변경
            now = 'N'
        row += 1    # 아래로 1칸씩 이동하며 탐색
 
    print(f'#{case} {ans}')