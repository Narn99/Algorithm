# 미생물 격리
# 가장자리는 벽, 미생물이 벽에 닿으면 절반으로 감소하고 이동방향이 반대로 바뀜.
# 1시간마다 이동, 만약 미생물 군집끼리 만나면 합쳐지고 미생물이 더 많은 군집의 이동방향으로 감.
# 같은 칸에서 부딪혀야 합쳐지므로, 서로 지나치는건 합쳐지는게 아님.
# 2차원 배열에 넣어서 풀어야 하나? 그냥 리스트에 미생물 군집을 그냥 넣어서 풀어야 하나?
# ==> 2차원 배열로 풀면 너무 오래 걸리므로 그냥 리스트로 풀어야 함
 
dct = {1:2, 2:1, 3:4, 4:3}      # 방향 전환은 그냥 딕셔너리같은 테이블로 하는게 빠르다
di = [0, -1, 1, 0, 0]
dj = [0, 0, 0, -1, 1]       # 방향은 1부터이므로 0번 인덱스에 0,0 넣어줌
 
T = int(input())
 
for case in range(1, T+1) :
 
    N, M, K = map(int, input().split())
    arr = []
    check = [0, N-1]
    for _ in range(K) :     # 배열에 미생물 정보 전부 저장
        arr.append(list(map(int,input().split())))
 
    for _ in range(M) :     # 0부터 M까지 시간 진행
        for i in range(len(arr)) :
            arr[i][0] += di[arr[i][3]]      # 미생물마다 1칸씩 이동
            arr[i][1] += dj[arr[i][3]]
            if arr[i][0] in check or arr[i][1] in check :   # 경계면에 도착했을 경우
                arr[i][2] //= 2
                arr[i][3] = dct[arr[i][3]]
        # 같은 좌표의 큰 미생물수부터 나오게 내림차순 정렬, 좌표가 같을 경우 앞에꺼에 더해주고 pop하면 되니까
        arr.sort(key=lambda x:(x[0],x[1],x[2]),reverse=True)
        k = 1   # 정리를 위한 인덱스
        while k < len(arr) :
            if arr[k][0] == arr[k-1][0] and arr[k][1] == arr[k-1][1] :  # 좌표가 같다면,
                arr[k-1][2] += arr[k][2]     # 앞에꺼에 미생물을 합쳐주고 pop해서 없애줌
                arr.pop(k)
                continue      # 뒤에꺼가 앞으로 당겨지므로, 인덱스가 더 나아가지 않도록 continue
            k += 1
 
    ans = 0
    for i in range(len(arr)) :  # 모두 끝난 뒤, 미생물 숫자 합산
        ans += arr[i][2]
 
    print(f'#{case} {ans}')