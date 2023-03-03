# 단순 2진 암호코드
# 7개의 자리수는 상품 고유의 번호, 마지막 자리는 검증 코드
# 암호 각 마지막 열은 1이니까.. 마지막이 1인 곳을 찾아서 거기서부터 앞으로 56개 탐색
# 7개씩 잘라서 숫자 판독하고, 그 뒤에 암호코드가 정상적인 암호인가 판별.
 
num = {'0001101' : '0', '0011001' : '1', '0010011' : '2', '0111101' : '3', '0100011' : '4', '0110001' : '5', \
       '0101111' : '6', '0111011' : '7', '0110111' : '8', '0001011' : '9'}
 
T = int(input())
 
for case in range(1, T+1) :
 
    N, M = map(int,input().split())
    arr = [input() for _ in range(N)]
    ei, ej = -1, -1
 
    for i in range(N) :
        for j in range(M-1, -1, -1) :
            if arr[i][j] == '1' :
                ei, ej = i, j       # 맨 뒷 열부터 1을 찾기
                break
        if ej != -1 :
            break
 
    num_st = ''
 
    for j in range(8) :     # 맨 뒤의 1부터 7개씩 슬라이싱해서 나눠주고,
        now = arr[ei][ej - (7*j+6) : ej - (7*j-1)]
        num_st += num[now]      # 만들어둔 딕셔너리에서 해당 밸류 값으로 바꿔 넣어주기
    num_st = num_st[::-1]       # 뒤에서부터 구했으니까 리스트 순서 한 번 뒤집어주기
 
    password = 0
    odd, even = 0, 0
 
    for i in range(7) :
        if i % 2 == 0 :     # 처음이 첫번째 숫자니까 0번 인덱스가 첫번째인 것,
            odd += int(num_st[i])   # 즉 홀수번째는 짝수번 인덱스를 넣어주면 된다.
        else :
            even += int(num_st[i])
 
    password = 3 * odd + even + int(num_st[-1])   # 암호 계산
 
    if password % 10 == 0 :
        ans = odd + even + int(num_st[-1])   # 10으로 나눠지면 총합을 출력, 아니면 0 출력
    else :
        ans = 0
    print(f'#{case} {ans}')