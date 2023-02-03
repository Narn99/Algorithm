for case in range(10) :

    dump = int(input())
    boxes = list(map(int,input().split()))
    
    # 가장 높고 낮은게 여러개여도 순서 상관없이 아무데나 옮겨도 된다고 하니까 카운팅으로
    # boxes를 카운팅, 가장 높은 항에서 1을 빼고 2번째로 높은 항에 1을 더하고,
    # 가장 낮은 항에서 1을 빼고, 2번째로 낮은 항에 1을 더해주는 식으로

    cnt = [0] * 100                         # 박스 높이별 갯수 카운팅할 리스트 cnt

    for i in range(100) :
        cnt[boxes[i]-1] += 1                # 박스 높이 한 번마다 cnt에 1씩 더해준다

    maxc = 0                                # 가장 높은 탑의 위치와 낮은 탑의 위치
    minc = 100

    for i in range(dump) :                  # dump번 수행하는 for문
        if maxc == minc or maxc == minc + 1 :
            break                           # 만약 높은 탑과 낮은 탑의 위치가 갖거나, 1개 차이면 종료
        for j in range(99, 0, -1) :
            if cnt[j] > 0 :                 # cnt의 뒤에서부터 0보다 큰 요소(= 현재 가장 큰 높이의 상자탑)가 있다면,
                cnt[j] -= 1                 # 가장 높은 상자탑에서 1을 빼고, 2번째로 높은 탑에 1을 더해준다
                cnt[j-1] += 1               # (= 가장 높은 상자탑에서 상자를 하나 뺐으니, 한 칸 낮아진 것)
                maxc = j
                for k in range(100) :
                    if cnt[k] > 0 :         # 마찬가지로 앞에서부터 0보다 큰 요소(= 현재 가장 낮은 높이의 상자탑)이 있다면,
                        cnt[k] -= 1         # 거기서 1을 빼고, 2번째로 낮은 탑에 1을 더해준다.
                        cnt[k+1] += 1
                        minc = k
                        break               # 1번 작업 했으니 break로 세번째 중첩된 for문 탈출
                break                       # 이어서 두번째 중첩된 for문 탈출

    maxV = 0
    minV = 0

    for i in range(100) :
        if cnt[i] > 0 :                     # 작업 이후, 최고탑과 최저탑을 구한다.
            minV = i
            break                           # cnt의 앞에서, 뒤에서 처음으로 1 이상 값이 있는 곳의 인덱스가 최저, 최고값들임
    for i in range(99, 0, -1) :
        if cnt[i] > 0 :
            maxV = i
            break

    V = maxV - minV

    print(f'#{case+1} {V}')

