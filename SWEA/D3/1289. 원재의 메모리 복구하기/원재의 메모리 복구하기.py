# 원재의 메모리 복구하기
# bit 중 하나를 0이나 1로 설정하면 끝까지가 전부 그 값으로 바뀜
# 자리수별로 진행하며, 한 자리에서 바꾸면 그 뒤로 전부 바뀌는 것을 생각하는데..
# 종료조건이 끝까지 가서 모양이 같고, 변형횟수가 최소인 것.
 
def dfs(n, cnt) :
    global mn
 
    if n == len(goal) :
        if start == goal :  # 끝까지 도달해서, 모양이 같고, 변경 횟수가 더 작으면 갱신
            if cnt < mn :
                mn = cnt
        return
    else :
        if start[n] == goal[n] :
            dfs(n+1, cnt)       # 안 하고 넘기기
        if start[n] != goal[n] :
            if start[n] == 0 :
                for i in range(n, len(goal)) :    # 현재 자리수가 0일 때 바꾸고 넘기기
                    start[i] = 1
                dfs(n+1, cnt+1)
            else :
                for i in range(n, len(goal)) :    # 1일 때 바꾸고 넘기기
                    start[i] = 0
                dfs(n+1, cnt+1)
    return
 
T = int(input())
 
for case in range(1, T+1) :
 
    goal = list(map(int,list(input())))
    start = [0]*len(goal)
    mn = 51
 
    dfs(0, 0)
 
    print(f'#{case} {mn}')