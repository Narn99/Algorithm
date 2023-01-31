N = int(input())

numlst = list(map(int,input().split()))             # N, 정수 리스트, v를 입력받는다

v = int(input())

count = 0                                           # 갯수를 셀 count를 0으로 설정

for num in numlst :
    if v == num :                                   # 만약 v와 정수 리스트의 수가 같다면 count에 1 추가하고 마지막엔 출력
        count += 1

print(count)