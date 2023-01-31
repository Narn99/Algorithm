N = int(input())

max_score = 0                                   # 최고점수를 넣어줄 값을 우선 0으로 설정

scores = list(map(int,input().split()))         # 점수들을 입력받아, 정수형으로 리스트화해서 할당한다.

for score in scores :
    if score > max_score :                      # for문으로 점수들 중에서 최고점수를 구해서 할당한다.
        max_score = score

cheated = []                                    # 조작한 점수를 넣어줄 빈 리스트 작성

for score in scores :
    cheated += [score / max_score * 100]        # 조작한 점수를 빈 리스트에 넣어준다

result = sum(cheated) / N                       # 조작한 점수의 합을 시험의 갯수 N으로 나눠 평균을 구하고 출력

print(result)