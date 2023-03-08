# 회의실 배정
# 회의 시간 배치로 최대한 많이 회의할 수 있는 회의 개수

import sys

N = int(sys.stdin.readline())
meet = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]
meet = sorted(meet, key=lambda x : (x[1], x[0]))    # 끝나는 시간이 빠른 순, 그 뒤 시작이 빠른 순으로 정렬

cnt = 1
end = meet[0][1]    # end의 시작은 가장 빨리 끝나는 회의의 시간

for i in range(1,N) :
    if meet[i][0] >= end :  # 시작 시간이 현 end보다 더 뒤라면 그 회의의 end로 갱신
        cnt += 1
        end = meet[i][1]

print(cnt)