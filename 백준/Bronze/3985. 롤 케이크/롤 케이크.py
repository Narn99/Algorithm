# 롤 케이크
# 1~N번까지 있는 방청객이, 1부터 L번까지 있는 롤케이크에서 원하는 P~K 조각을 냄.
# 1번 방청객부터 해당 조각에 그 사람 번호를 적으며, 이미 번호가 있는 조각엔 못 적음(visit)

cake = [0]*(int(input())+1)
people = int(input())
pre_mx, pre_person = 0, 0
real_mx, real_person = 0, 0

for i in range(1, people+1) :
    P, K = map(int,input().split())
    pre = K-P+1
    if pre > pre_mx :       # 가장 많이 받을거라 예측된 사람
        pre_mx = pre
        pre_person = i
    for j in range(P, K+1) :
        if cake[j] == 0 :
            cake[j] = i

for i in range(1, people+1) :
    cnt = 0
    for j in cake :
        if j == i :
            cnt += 1
    else :
        if cnt > real_mx :  # 실제 많이 받은 사람
            real_mx = cnt
            real_person = i

print(pre_person)
print(real_person)