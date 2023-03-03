# Contact
# 연락 시작 당번과 비상연락망이 주어질 때, 가장 나중에 연락받는 사람 중 번호가 큰 사람. (연결 안 됐으면 못 받음)
# BFS로 풀었을 때, 마지막 회차에서 번호가 가장 큰 놈 구하기.
 
tc = 1
 
while True :
    try :
        dat, S = map(int,input().split())
        tel = [[] for _ in range(101)]
        lst = list(map(int,input().split()))
        for i in range(len(lst)//2) :           # 0과 짝수번이 from, 홀수번이 to
            tel[lst[2*i]].append(lst[2*i+1])
        same_cnt = [[] for _ in range(dat+1)]   # 같은 이동거리의 번호들 비교하기 위한 리스트
        ans = 0
        cnt = 0
        Q = [(S, cnt)]
        visited = []    # 이미 연락 받은 사람
 
        while True :
            if Q :
                now, cnt = Q.pop(0)
                same_cnt[cnt].append(now)
            else :
                break                       # 큐가 비어있다 = 더 이상 연락 불가일 때 종료
            for i in tel[now] :
                if i not in visited :
                    Q.append((i, cnt+1))    # 전화받을 사람과 연락 거리를 큐에 추가
                    visited.append(i)       # 받는 사람 번호를 visited에 추가
 
        for last in same_cnt[cnt] :
            if last > ans :
                ans = last
 
        print(f'#{tc} {ans}')
        tc += 1
 
 
    except :
        break