# 영식이와 친구들
# 1번부터 다른 사람에게 공을 던지며, 한 사람이 M번 받게 되면 끝
# 자기가 공을 받은 횟수가 홀수면 오른쪽으로 L, 짝수면 왼쪽으로 L번째 사람에게 던지기

N, M, L = map(int,input().split())

Q = [0]*N
idx = 0
cnt = 0

while True :
    Q[idx] = Q[idx] + 1     # 받은 횟수 1 증가
    if Q[idx] == M :
        break
    if Q[idx] % 2 == 1 :    # 홀수면 오른쪽
        idx = (idx+L) % N
        cnt += 1
    else :
        idx = (idx-L) % N   # 짝수면 왼쪽
        cnt += 1
        
print(cnt)
