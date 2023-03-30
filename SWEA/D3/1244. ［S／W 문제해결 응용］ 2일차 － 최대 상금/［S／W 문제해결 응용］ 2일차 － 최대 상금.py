# 최대 상금
# 정해진 교환 횟수만큼 행해서, 최대 상금값을 구하기
# 각 자리 바꾼걸 일일이 확인하는데.. tmp라는 임시 리스트를 만들어서 확인.
# tmp의 인덱스는 교환 횟수. 그 횟수의 교환했을 때 최댓값이 되는 값을 저장해가며 진행.
# 항상 최댓값을 확보해두고 tmp의 마지막 인덱스 값을 뽑아내기.

def check(n, lst) :
    global ans
    if n == change :            # 교환 전부 했으면 종료
        return
    else :
        for i in range(ln-1) :  # i와 j를 교환하고, 그 수랑 tmp에 저장된 값이랑 비교해서 갱신
            for j in range(i, ln) :
                if i != j :     # 무조건 교환해야하니 i != j를 넣어줌. 안 넣으면 i == j가 최대일 때 생김.
                    lst[i], lst[j] = lst[j], lst[i]
                    num = int(''.join(lst))
                    if  num > tmp[n] :
                        tmp[n] = num
                        check(n+1, lst)
                    lst[i], lst[j] = lst[j], lst[i]

T = int(input())

for case in range(1, T+1) :

    a, b = input().split()
    nums = list(a)
    change = int(b)
    ln = len(nums)
    tmp = [0]*change

    check(0, nums)

    ans = tmp[-1]

    print(f'#{case} {ans}')