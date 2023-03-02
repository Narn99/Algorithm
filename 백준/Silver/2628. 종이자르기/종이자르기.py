# 종이자르기
# 가로 세로가 잘리는 부분을 전부 기록하고, 
# 정렬된 상태에서 ((n+1)-n)*((m+1)-m) << 인덱스로 따지면 이런 느낌으로 사이 넓이들 구하며 최댓값

garo, sero = map(int,input().split())
paper = [[0]*garo for _ in range(sero)]
N = int(input())

z = [0, sero]
o = [0, garo]

for i in range(N) :
    D, num = map(int, input().split())
    if D == 0 :
        z.append(num)
    else :
        o.append(num)

z.sort()
o.sort()
mx = 0

for i in range(len(z)-1) :
    for j in range(len(o)-1) :
        area = (z[i+1]-z[i])*(o[j+1]-o[j])
        if area > mx :
            mx = area

print(mx)