word = list(input())

cnt = 0                       # cnt가 늘어나는만큼 전체 글자수를 줄여준다고 생각하면 된다.

for i in range(len(word)-1) :
    if word[i:i+2] == ['c', '='] or word[i:i+2] == ['c','-'] :
        cnt += 1
    elif word[i:i+2] == ['d','-'] or word[i:i+2] == ['l','j'] :
        cnt += 1
    elif word[i:i+2] == ['n','j'] or word[i:i+2] == ['s','='] :
        cnt += 1
    elif word[i:i+2] == ['z','='] :
        cnt += 1                   # 여기는 2글자가 1글자가 되는거니 +1씩

for i in range(len(word)-2) :
    if word[i:i+3] == ['d','z','='] :
        cnt += 1                   # 여기는 이미 z=로 +1 된 상태에서 1글자 더 추가하는거니 +1

print(len(word)-cnt)               # 전체 글자수에서 cnt만큼을 빼주면 된다.