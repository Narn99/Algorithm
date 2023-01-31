remainder = {}                      # 나머지들의 빈 딕셔너리 생성

for nums in range(10) :
    num = int(input()) % 42         # 10가지 정수를 입력받으며 42로 나눈 나머지를 할당
    if num in remainder :
        remainder[num] += 1         # 만약 그 나머지를 key로 하는 값이 이미 딕셔너리에 있다면 value에 1 추가
    else :
        remainder[num] = 1          # 딕셔너리에 없는 상태라면 value를 1로 하여 추가
    
print(len(remainder.keys()))        # 나머지들의 딕셔너리의 key들의 갯수를 출력하면, 나머지가 서로 다른 수들의 갯수를 구할 수 있다.