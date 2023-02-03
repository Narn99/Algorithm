T = int(input())                            # 테스트 케이스의 갯수 T 입력

for case in range(T) :
    N = int(input())                        # 분해시킬 정수 N 입력

    a, b, c, d, e = 0, 0, 0, 0, 0           # 2, 3, 5, 7, 11의 지수인 a, b, c, d, e를 전부 0으로 시작

    while True :
        if N % 2 == 0 :                     # while문 반복으로 2, 3, 5, 7, 11로 나눠지는 한 계속 그 지수에 1을 추가해가며 나눠준다.
            a += 1
            N = N // 2
        elif N % 3 == 0 :
            b += 1
            N = N // 3
        elif N % 5 == 0 :
            c += 1
            N = N // 5
        elif N % 7 == 0 :
            d += 1
            N = N // 7
        elif N % 11 == 0 :
            e += 1
            N = N // 11
        else :
            break                           # 더는 나눌 수 없을 때, while문 종료

    print(f'#{case+1} {a} {b} {c} {d} {e}') # 양식에 맞게 출력
