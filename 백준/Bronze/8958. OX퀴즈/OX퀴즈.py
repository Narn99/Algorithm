# 리스트화해서 이전 요소랑 비교, 같다면 이전 요소의 수에 1을 더하는 또 다른 리스트를 작성
# 예를 들면, 입력값이 OXOOXOOO라면, [1,0,1,2,0,1,2,3] 이라는 리스트를 만들어서 계산

N = int(input())


for num in range(N) :

    testlst = list(input())

    result = []

    if testlst[0] == 'O' :                                          # 첫 원소가 'O'라면 result 리스트에 1을 넣어주고, 아니라면 0을 넣어줌
        result += [1]
    else :
        result += [0]

    for OX in range(1,len(testlst)) :
        if testlst[OX] == 'O' :                                     # 입력받은 OX를 리스트로 만든 testlst를 순회하며, 현재 자리가 'O'라면 그 전 자리와 비교한다.
            if testlst[OX] == testlst[OX-1] :                       # 그 전 자리도 'O'라면 그 전 자리의 result 리스트에, 그 전 자리의 수에 1을 더해서 넣어준다.
                result += [result[OX-1]+1]
            else :
                result += [1]                                       # 그 외라는 것은, 그 이전 자리는 'O'가 아니라는 것이므로 1을 넣어준다.
        else : 
            result += [0]                                           # 현재 자리가 'X'라면 0을 넣어준다.

    print(sum(result))                                              # teslst의 자리수에 맞춰 만든 result 리스트의 합계를 출력.