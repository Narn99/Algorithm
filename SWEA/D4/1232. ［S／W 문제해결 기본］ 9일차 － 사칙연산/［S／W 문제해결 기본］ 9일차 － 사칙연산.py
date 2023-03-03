# 사칙연산 ~ 후위순회 or 그냥 리프 노드부터 탐색해서 연산자 발견하면 그 자식 노드들을 연산하기
 
T= 10
for case in range(1, T+1) :
 
    N = int(input())
    nodes = [-1]*(N+1)
    c1 = [-1]*(N+1)
    c2 = [-1]*(N+1)
 
    for _ in range(N) :
        info = input().split()
        if len(info) == 4 :     # 연산자가 들어있는건 길이가 4
            a, b, c = map(int,[info[0],info[2],info[3]])
            nodes[a] = info[1]
            c1[a] = b
            c2[a] = c
        else :
            e,f = map(int,info)   # 숫자만 있는 노드는 길이가 다들 2
            nodes[e] = f
 
    for i in range(N-1, 0, -1) :     # 밑에서부터 연산하는거니까 N-1부터
        if nodes[i] == '+' :
            nodes[i] = nodes[c1[i]] + nodes[c2[i]]
        elif nodes[i] == '-' :
            nodes[i] = nodes[c1[i]] - nodes[c2[i]]
        elif nodes[i] == '*' :
            nodes[i] = nodes[c1[i]] * nodes[c2[i]]
        elif nodes[i] == '/' :
            nodes[i] = nodes[c1[i]] // nodes[c2[i]]
 
    print(f'#{case} {nodes[1]}')