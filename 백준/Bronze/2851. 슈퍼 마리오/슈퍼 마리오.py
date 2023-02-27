# 슈퍼 마리오
# 버섯 먹어서 최대한 100에 가깝게 만들기. (합 - 100의 절대값이 가장 작은 것)

sm = 0

for _ in range(10) :

    mush = int(input())
    new = sm + mush

    if abs(new-100) <= abs(sm-100) :
        sm = new
    else :
        break

print(sm)