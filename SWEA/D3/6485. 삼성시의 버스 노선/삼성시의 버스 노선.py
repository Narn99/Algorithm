T = int(input())                                    # 테스트 케이스 갯수 T

for case in range(T) :

    N = int(input())                                # 버스 노선 갯수 N

    AB = []                                         # 버스 노선 번호 a, b가 가는 곳 넣어줄 빈 리스트 AB

    for i in range(N) :
        a, b = map(int,input().split())             # N번 반복하며, i번째 a와 b 값을 입력받는다.
        ab = []
        for num in range(a, b+1) :                  # Ai 이상, Bi 이하 => a 이상, b 이하인 값들을 리스트화해서 ab 리스트에 넣어준다.
            ab += [num]
        AB += [ab]                                  # 그 리스트 ab를 AB 리스트에 다시 넣어준다. (A1~B1, A2~B2 같은 식으로 정리된 리스트)

    P = int(input())                                # 버스 정류장 갯수 P

    C = []                                          # 버스 정류장의 번호들 넣어줄 리스트 C

    for j in range(P) :
        C += [int(input())]                         # 버스 정류장의 번호들을 입력받아 C에 넣어준다

    result = [0]*P                                  # 결과값으로 쓸 리스트를 초기 값들을 전부 0으로, P개의 항이 있는 리스트로 만들어준다.

    for i in range(N) :
        for j in range(P) :                         # j번째 버스 정류장의 번호가 i번째 버스 노선에 들어있다면, j번째 result의 요소의 값에 1을 더해준다.
            if C[j] in AB[i] :
                result[j] += 1

    print(f'#{case+1}', end=' ')                    # 양식에 맞게 출력해준다.
    for num in result :
        print(num, end=' ')
    print('')