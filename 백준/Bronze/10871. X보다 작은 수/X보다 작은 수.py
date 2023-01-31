nx = list(map(int,input().split()))             # 정수 N과 X를 입력받아서 리스트에 저장

numlst = list(map(int,input().split()))         # 정수를 N개 입력받아 리스트로 저장

for num in numlst :                             # numlst로 받아둔 정수들을 X와 비교해서 띄어쓰기를 구분자로 출력해주는 반복문을 작성
    if num < nx[1] :
        print(num,end=' ')
