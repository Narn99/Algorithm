# 파스칼의 삼각형
# 첫째 줄은 1, 두번째 줄부터 각 숫자는 왼쪽과 오른쪽 위의 숫자의 합으로 구성.
# -> 모든 줄 양 끝은 1뿐이고, n번째 줄의 m번째 숫자는, n-1번째 줄의 m-1번째와 m번째 숫자를 합친 것.
 
T = int(input())
 
for case in range(1, T+1) :
 
    N = int(input())
    arr = [[1]]     # 가장 윗 줄은 1
 
    for i in range(1, N) :
        stk = [1]           # 줄마다 첫 요소는 1인 리스트를 만든다.
        for j in range(1, i+1) :
            try :           # 현재 줄의 두번째 수부터 윗 줄의 j-1번째 요소와 j번째 요소를 합친게 현재 위치의 값
                stk += [arr[i-1][j-1] + arr[i-1][j]]
            except :
                stk += [1]  # 줄마다 마지막 요소는 1
        else :
            arr += [stk]    # 만든 리스트(줄)을 배열에 넣어준다
 
    print(f'#{case}')
    for i in range(N) :
        print(' '.join(map(str,arr[i])))