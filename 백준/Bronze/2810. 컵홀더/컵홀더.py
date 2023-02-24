# 컵홀더
# 010101010 (좌석이 1이라면 컵 홀더가 0인 식으로 배치), 커플석 사이엔 컵 홀더가 없음.
# 정답 계산은 S를 만나면 +1, L을 만나면 1칸 건너뛰고 +1
# LL S LL

N = int(input())
line = list(input())
idx = 0
holder = 1

while idx < N :
    if line[idx] == 'S' :
        holder += 1
        idx += 1
    else :
        holder += 1
        idx += 2

if holder >= N :    # 홀더가 사람보다 많으면 사람만큼
    print(N)
else :
    print(holder)