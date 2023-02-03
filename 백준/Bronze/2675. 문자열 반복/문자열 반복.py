T = int(input())

for case in range(T) :

    S = input().split()
    R = int(S[0])
    Slst = list(S[1])

    for i in Slst :
        print(i*R, end='')
    print('')