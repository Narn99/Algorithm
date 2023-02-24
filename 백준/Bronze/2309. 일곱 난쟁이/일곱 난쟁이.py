# 일곱 난쟁이 ~ 부분집합의 합 ~ 9명의 난쟁이 중 7명 골라 100이 되는 조합 고르기, 오름차순

def check(n, sm, lst, cnt) :
    global ans
    if sm > 100 :
        return
    if cnt > 7 :
        return
    if n == 9 :
        if cnt == 7 :
            if sm == 100 :
                ans += [[i for i in lst]]
        return
    lst.append(dwarfs[n])
    check(n+1, sm+dwarfs[n], lst, cnt+1)
    lst.pop()
    check(n+1, sm, lst, cnt)

dwarfs = [int(input()) for _ in range(9)]
ans = []
check(0, 0, [], 0)
ans[0].sort()

for i in ans[0] :
    print(i)