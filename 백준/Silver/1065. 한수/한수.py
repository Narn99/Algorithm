N = int(input())

i = 1
cnt = 0

while i <= N :                                      # i에 1 더해가며 N이 될 때까지 반복

    if i < 10 :
        cnt += 1                                    # 만약 i가 한자리 숫자면 그냥 cnt에 1 더하기

    lst = list(map(int,list(str(i))))

    check = 0

    for j in range(1, len(lst)-1) :                 # j번째에서 j-1번째를 뺀 값이, j+1번째에서 j번째를 뺀 값과 같다면
        if lst[j] - lst[j-1] == lst[j+1] - lst[j] : # check에 1을 더해줌
            check += 1

    if check == len(lst) - 2 :                      # 만약 check가 현재 i의 길이보다 2가 작다면 (3개씩 묶어서 셌으니까)
        cnt += 1                                    # cnt에 1을 더해줌

    i += 1

print(cnt)
