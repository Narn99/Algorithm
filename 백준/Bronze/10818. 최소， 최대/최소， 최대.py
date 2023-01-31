N = int(input())

numlst = list(map(int,(input().split())))       # 정수 리스트로 입력받기

minn = 1000000                                  # 최솟값과 최댓값을 최소치와 최대치로 시작
maxn = -1000000

for num in numlst :                             # 리스트의 요소를 돌며 최솟값과 최댓값을 계산해서 저장
    if num < minn :
        minn = num
    if num > maxn :
        maxn = num
    
print(minn, maxn)                         # 최솟값과 최댓값 출력