# 중위순회
 
def inorder(n) :
    global visit
    if n :
        if c1[n] != -1 :
            inorder(c1[n])
        visit += alp[n]     # visit이 가운데, 알파벳을 넣어주자
        if c2[n] != -1 :
            inorder(c2[n])
 
T = 10
 
for case in range(1, T+1) :
 
    N = int(input())
    alp = ['']*(N+1)
    c1 = [-1]*(N+1)
    c2 = [-1]*(N+1)
    visit = ''
 
    for i in range(N) :
        A = input().split()
        p = int(A[0])
        alp[p] = A[1]
        if len(A) >= 3 :
            c1[p] = int(A[2])
        if len(A) == 4 :
            c2[p] = int(A[3])
 
    inorder(1)
 
    print(f'#{case} {visit}')