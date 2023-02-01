C = int(input())                                # 테스트 케이스 갯수 C 입력

for case in range(C) :

    lst = list(map(int,input().split()))        # 각 케이스의 줄마다 입력받은 값을 리스트로 저장
    N = lst[0]                                  # 리스트의 첫 항이 학생의 수 N
    scores = lst[1:]                            # 리스트의 두번째 항부터 끝까지를 학생들의 점수로 리스트 scores에 저장한다

    if N == 0 :                                 # 만약 N이 0이라면 ZeroDivisionError 발생하니
        pass

    else :
        aver = sum(scores) / N                      # 학생들의 점수의 평균 aver를 저장
        over_aver = 0                               # 평균이 넘는 학생들의 수를 계산할 over_aver를 0으로 시작

        for score in scores :
            if score > aver :                       # 점수들 중에서 평균을 넘는 점수가 있을 때마다 over_aver에 1을 더해준다
                over_aver += 1

        percent = over_aver/N*100                   # 평균이 넘는 학생의 비율을 백분율로 소수점 3째자리까지 바꿔줌

        print(f'{percent:.3f}%')                     # 양식에 맞게 출력