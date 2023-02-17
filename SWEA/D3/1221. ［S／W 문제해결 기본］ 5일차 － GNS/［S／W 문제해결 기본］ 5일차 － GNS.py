# GNS
# 0~9가 문자열로 치환되는 행성, 문자열을 받아 작은 수부터 정렬해서 출력하기
# 일단 ZRO부터 NIN까지 순서대로 정렬해놓은 리스트를 만들어놓자.
# 1. 정렬 리스트를 앞에서부터 순회하며, 케이스에서 해당 문자들을 찾는대로 다른 배열에 넣는 방법
# 2. 딕셔너리로 문자별 개수 정리해서, 새 배열에 그 문자의 개수만큼 채워넣는 방법 <- 이거로 해보기
 
numbers = ['ZRO', 'ONE', 'TWO', 'THR', 'FOR', 'FIV', 'SIX', 'SVN', 'EGT', 'NIN']
 
T = int(input())
 
for case in range(T) :
 
    t, N = input().split()
    N = int(N)
    lst = list(input().split())
    numdic = {}
    ans = []
 
    for i in range(N) :
        if lst[i] in numdic :
            numdic[lst[i]] += 1         # 문자를 key값, value를 개수로 세주기
        else :
            numdic[lst[i]] = 1
 
    for num in numbers :
        ans += [num] * numdic[num]      # numbers 리스트 순서대로 ans에 문자를 개수만큼 넣어주기
 
    print(t)
    for i in range(N) :
        print(ans[i],end=' ')    
    print()