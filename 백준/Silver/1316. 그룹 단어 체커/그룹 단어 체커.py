N = int(input())

total = 0

for case in range(N) :

    word = list(input())

    # 처음 등장하면 분류해서 놓고, 앞에거랑 같다면 ok, 이미 있는데 등장해서 앞에거랑 다르다면 no

    check = [word[0]]
    total += 1                          # 정상 진행된다면 이번 반복에 total은 +1이 될 것

    for i in range(1,len(word)) :
        if word[i] not in check :
            check += [word[i]]          # check 리스트에 안 들어있는 글자면 넣어줌.
        elif word[i] in check :
            if word[i] == word[i-1] :
                continue                # check에 있는 글자면, 바로 앞에 글자랑 같다면 continue
            else :
                total -= 1              # 앞에 글자랑 다르다면 total을 0으로 만들어준다.
                break

print(total)