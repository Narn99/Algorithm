N = int(input())
i = 1               # i가 지나는 방의 갯수
n = 1

while True :
    if N == 1 :
        i = 1
        break
    if n >= N :
       break        # 1+6*(i) 안에 있는거니까, 그것보다 작으면 끝내기
    n += 6*(i)
    i += 1

print(i)