# 간단한 압축 풀기 ~ 너비가 10인 문자열, 연속된 알파벳은 AAA => A3 과 같은 식으로 개수로 압축
# 압축된 문서를 원본문서로 만들기
# 알파벳 * 개수로 넣어주는데, 길이가 10에 도달하면 다음줄로 넘기기
 
T = int(input())
 
for case in range(T) :
 
    N = int(input())
    cnt = 0
    print(f'#{case + 1}')
    for word in range(N) :
        letter, num = input().split()
        num = int(num)
        cntnum = 0
        while True :
            print(letter, end='')
            cnt += 1                # 그 줄의 길이 개수 세기
            cntnum += 1             # 알파벳 입력 개수 세기
            if cntnum == num :      # 알파벳 다 입력했으면 종료
                if cnt >= 10 :      # 만약 그 줄의 10번째 글자였으면 엔터 한 번하고 위치 초기화
                    print()
                    cnt = 0
                break
            elif cnt >= 10 :        # 만약 그 줄의 10번째 글자면 엔터치고 위치 초기화
                print()
                cnt = 0
    if cnt != 0 :                   # 현재 입력 위치가 0번째가 아니라면 마지막이 end=''로 끝났을거라,
        print()                     # 다음 순회를 그 다음 줄부터 출력하기 위해 엔터 한 번