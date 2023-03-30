# 정식이의 은행업무
# 금액을 2진수, 3진수의 형태로 기억하고 다니는데, 각각 단 한 자리만을 잘못 기억하고 있다.
# 받은 2진수와 3진수에서 각각 자리의 수를 바뀐걸 전부 구하고 비교해서 같은거 찾기?
# 받은 수를 십진수로 바꾼 뒤에, 원래 있던 2진수와 3진수에서 자리수 바꾸기(빼기 혹은 더하기)한 값들
# 따로 리스트에다 기록해뒀다가 비교해보기?

T = int(input())

for case in range(1, T+1) :

    bi = input()
    tri = input()
    bl = len(bi)
    tl = len(tri)

    bi_num = int(bi, 2)    # 현재의 이진수 값을 십진수로 바꿨을 때의 값 구하기
    tri_num = int(tri, 3)    # 현재의 삼진수 값을 십진수로 바꿨을 때의 값 구하기

    # 현재의 이진수, 삼진수에서 자리수 1개만 바꿨을 때의 값들 리스트 찾아서 저장
    bi_lst = []
    tri_lst = []
    for i in range(bl) :    # bi_lst에 자리수가 1이면 0으로 했을 때 값과, 0이면 1로 했을 때 값을 저장
        if bi[bl-i-1] == '1':
            bi_lst.append(bi_num - (2 ** i))
        else:
            bi_lst.append(bi_num + (2 ** i))

    for i in range(tl) :    # tri_lst에도 마찬가지로 자리수가 다를 때의 값을 저장하기
        if tri[tl-i-1] == '2' :
            tri_lst.append(tri_num - (3**i))
            tri_lst.append(tri_num - (2*(3**i)))
        elif tri[tl-i-1] == '1' :
            tri_lst.append(tri_num + (3**i))
            tri_lst.append(tri_num - (3**i))
        else :
            tri_lst.append(tri_num + (2*(3**i)))
            tri_lst.append(tri_num + (3**i))

    for num in bi_lst :      # 바꾼 값들의 리스트에서 공통인 숫자 찾아서 출력
        if num in tri_lst :
            print(f'#{case} {num}')
            break