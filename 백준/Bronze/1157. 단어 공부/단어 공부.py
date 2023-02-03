from string import ascii_lowercase

alphabet = list(ascii_lowercase)

cnt = [0]*len(alphabet)

word = list(input().lower())

for i in range(len(alphabet)) :
    for j in word :
        if alphabet[i] == j :       # 알파벳이 단어에 있으면 cnt의 같은 인덱스에 카운팅
            cnt[i] += 1

maxa = 0
maxw = ''

for i in range(len(cnt)) :
    if cnt[i] > maxa :
        maxa = cnt[i]
        maxw = alphabet[i]          # 가장 많이 사용된 횟수와 그 알파벳을 저장

maxcnt = 0

for i in cnt :
    if i == maxa :
        maxcnt += 1                 # 만약 가장 많이 사용된 알파벳이 2개 이상이면 ? 출력

if maxcnt > 1 :
    print('?')
else :
    print(maxw.upper())