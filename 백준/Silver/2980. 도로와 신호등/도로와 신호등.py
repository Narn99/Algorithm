# 도로와 신호등
# 길이 L의 1차 배열, 중간 중간 N개의 신호등이 있음. DP로 그냥 이동하며 풀자

N, L = map(int,input().split())
place = 0   # 현재 위치
time = 0

for i in range(N) :
    D, R, G = map(int, input().split())
    time += D - place   # D까지 이동하는데 걸린 시간 추가
    place = D
    waste_time = time % (R+G)   # 빨간불 바뀌기 기다리는 시간
    if waste_time < R :
        time += R - waste_time
else :
    time += L - place

print(time)