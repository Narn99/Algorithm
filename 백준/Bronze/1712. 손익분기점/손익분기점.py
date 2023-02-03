A, B, C = map(int,input().split())

if B==C :
    print(-1)
elif A / (C-B) > 0 :
        print(A//(C-B) + 1)
else :
    print(-1)