students = []                           # 학생들을 넣어줄 빈 리스트 작성

for num in range(28) :
    students += [int(input())]          # 28 명의 출석번호를 받아 리스트에 넣어줌

badstudents = []                        # 제출 안 한 학생들 넣을 빈 리스트 작성

for stu_num in range(30) : 
    if stu_num+1 in students :          # 30까지 루프하며 제출한 학생들에 없는 번호를 뽑아서 리스트에 넣어줌
        pass
    else :
        badstudents += [stu_num+1]      # 여기서 알아서 작은 것부터 리스트에 들어간다.

print(badstudents[0])                   # 줄 나눠서 작은 것과 큰 것 순으로 출력
print(badstudents[1])