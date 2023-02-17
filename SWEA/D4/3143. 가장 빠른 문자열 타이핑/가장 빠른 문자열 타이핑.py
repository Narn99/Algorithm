# 가장 빠른 문자열 타이핑 ~ A라는 문자열 타이핑할 때, B에 저장된 문자열을 이용해 타자수를 줄인다.
# A 안에 B가 몇 개 있는지 찾고, B의 개수 + 나머지 = A 길이 - (B 길이 - 1) * B의 개수
 
T = int(input())
 
for case in range(T) :
 
    A, B = map(list,input().split())
    N, M = len(A), len(B)
    cnt = 0
    check = 0       # 만약 밑에서 if i <= check , check = i+M-1 라고 입력할거면, 여기서 0보다 작은 수로 해줘야됨.
 
    for i in range(N-M+1) :
        if i < check :     # 이거 안 넣으면, A : aaaaa, B : aa 같은거에서 A안에 B가 4개 있다고 세어버림
            continue        # 고로 A 안에서 B를 찾았으면, 그 B 이후의 위치로 넘어가줘야함.
        if B == A[i:i+M] :
            cnt += 1
            check = i+M
 
    ans = N - (M-1) * cnt
 
    print(f'#{case+1} {ans}')