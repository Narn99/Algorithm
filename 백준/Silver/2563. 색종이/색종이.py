# 색종이
# 가로세로 100인 사각형 흰색 도화지, 그 위에 가로세로 10인 사각형 검은색 색종이를 붙임
# 여러 장이 범위 겹쳐서 붙일 수도 있음. 0 요소들로 구성된 도화지에 검은색 붙이면 1씩 추가?
# 넓이란게 가로x세로이긴 한데, 그냥 0이 아닌 요소 개수 세면 넓이 나올듯

white = [[0]*100 for _ in range(100)]
black = int(input())

for case in range(black) :
    left, under = map(int,input().split())

    for row in range(10) :
        for col in range(10) :
            white[-under-row-1][left+col] += 1  # 색칠하기

cnt = 0
for row in range(100) :
    for col in range(100) :
        if white[row][col] != 0 :       # 색칠된 부분마다 cnt에 1 추가
            cnt += 1

print(cnt)