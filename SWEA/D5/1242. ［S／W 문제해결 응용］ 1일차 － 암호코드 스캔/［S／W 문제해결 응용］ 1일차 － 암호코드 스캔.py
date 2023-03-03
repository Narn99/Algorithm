# 암호코드 스캔
# 8자리 수, 앞 7자리는 상품번호, 마지막은 검증코드로 홀수*3 + 짝수 + 검증코드 = 10의 배수여야 함.
# 연속되는 0의 개수, 1의 개수를 번갈아 세면서 카운트 배열에 저장
# 그 카운트 배열을 4개씩 골라서, 그 뒤쪽 3개를 비교해서 암호번호를 찾는다. 그 암호번호로 검증코드 찾기
# 암호코드가 여러개? 암호가 만약 한 줄에 두개 있으면? => 한 줄을 다 뜯어내서 찾아봐야할 듯.
# 그걸 확인할 때 오른쪽 끝이 0으로 끝나면, 오른쪽 0을 지우고 왼쪽 앞에 붙여주기.
 
dct = {
    (2, 1, 1): 0,
    (2, 2, 1): 1,
    (1, 2, 2): 2,
    (4, 1, 1): 3,
    (1, 3, 2): 4,
    (2, 3, 1): 5,
    (1, 1, 4): 6,
    (3, 1, 2): 7,
    (2, 1, 3): 8,
    (1, 1, 2): 9,
}
 
T = int(input())
 
for case in range(1, T + 1):
 
    N, M = map(int, input().split())
    arr = list(set([input() for _ in range(N)]))    # set으로 중복되는 행들 제거
    ans = 0
    check = []
 
    for nums in arr :
 
        num = ''
        for i in range(M) :
            a = int(nums[i],16)         # 십육진수를 이진수로 변경
            for j in range(3, -1, -1):
                num += '1' if a & (1 << j) else '0'
 
        if '1' not in num : continue       # 0뿐인 행은 안 하고 넘기기
 
        num = num.rstrip('0') + '0'
        num = num.lstrip('0')       # 왼쪽과 오른쪽 0들 없애기(오른쪽 0은 하나만 남김)
 
        psw = ''
        cnt = odd = even = 0    # 숫자 8개, 홀수, 짝수 계산할 것들 
 
        n1 = n2 = n3 = 0    # 1, 0, 1 계산할 것들
        for i in range(len(num)):
            if num[i] == '1' and n2 == 0 :      # 첫 1의 개수 세주기
                n1 += 1
            elif num[i] == '0' and n1 != 0 and n3 == 0 : # 그 다음 0의 개수 세주기
                n2 += 1
            elif num[i] == '1' and n2 != 0 :    # 그 다음 1의 개수 세주기
                n3 += 1
            elif n3 != 0 :
                cnt += 1
                mn = min(n1,n2,n3)          # 센 숫자 3개 중 최솟값을 구하고,
                psw_num = dct[(n1//mn, n2//mn, n3//mn)] # 그 최솟값으로 각각을 나눠, 비율로 십진수 번호 찾기
                psw += str(psw_num)         # 그 번호를 임시 암호로 저장
                if cnt == 8 :
                    temp = odd * 3 + even + psw_num 
                    if temp % 10 == 0 and psw not in check:     # 정상 암호인지 검증하고 맞다면 정답에 포함
                        ans += odd + even + psw_num
                    check.append(psw)       # 이미 계산한거 아닌가 넣어주고,
                    psw = ''                # 계산에 쓴 것들 초기화
                    cnt = odd = even = 0
                elif cnt % 2 :
                    odd += psw_num  # 홀수
                else :
                    even += psw_num # 짝수
 
                n1 = n2 = n3 = 0    # 한 십진수 번호 구한거 초기화
 
    print(f'#{case} {ans}')