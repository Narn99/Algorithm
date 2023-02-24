# 방 배정
# 한 방에는 같은 학년의 같은 성별끼리 배정, 1명만 배정도 가능함

N, K = map(int,input().split()) # 학생 수 N, 한 방 최대 인원 K
boy = [0]*7
girl = [0]*7
room = 0

for stu in range(N) :
    gender, grade = map(int,input().split())
    if gender == 0 :
        girl[grade] += 1
    else :
        boy[grade] += 1

for stu in boy :        # 남자방
    if stu % K == 0 :
        room += stu//K
    else :
        room += stu//K + 1
for stu in girl :       # 여자방
    if stu % K == 0 :
        room += stu//K
    else :
        room += stu//K + 1

print(room)
