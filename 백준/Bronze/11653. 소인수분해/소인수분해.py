N = int(input())
cN = N

if N == 1 :
    pass
else :
    for i in range(2, N+1) :    # 어차피 2부터 나누는거니까
        while True :
            if cN % i == 0 :
                cN = cN // i
                print(i)
            else :
                break