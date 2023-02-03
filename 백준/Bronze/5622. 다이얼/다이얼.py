eng = [[], ['A','B','C'], ['D','E','F'], ['G','H','I'], ['J','K','L'], ['M','N','O'], ['P','Q','R','S'], ['T','U','V'], ['W','X','Y','Z'], []]

word = list(input())

cnt = 0

for i in range(len(word)) :
    for j in range(len(eng)) :
        if word[i] in eng[j] :          # 알파벳 인덱스까지 가는 시간.
            cnt += j+2                  # 0번 인덱스인 1을 누르는데 2초였으니, +2를 해준다.

print(cnt)
