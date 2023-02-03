from string import ascii_lowercase

alphabet = list(ascii_lowercase)          # 알파벳 리스트, 입력받은 단어의 글자 리스트, 체크용 리스트 만듦
S = list(input())
alphacheck = [0]*len(alphabet)

for i in range(len(alphabet)) :
    if alphabet[i] in S :
        for j in range(len(S)) :
            if alphabet[i] == S[j] :      # a~z의 알파벳을 순서대로 위치 파악
                if alphacheck[i] > 0:     # 있었다면 그 위치 j값 출력하고, 체크용 리스트의 그 알파벳 인덱스 값에 1 추가
                    pass                  # 만약 이미 체크용 리스트에서 0보다 큰 값을 갖고 있는 알파벳이라면 패스
                else:
                    print(j, end=' ')
                    alphacheck[i] += 1
    else :
        print(-1, end=' ')
