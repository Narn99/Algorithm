# 문자열의 거울상
 
T = int(input())
 
for case in range(T) :
 
    s = list(input())            # 리스트로 받기
 
    for i in range(len(s)) :
        if s[i] == 'p' :
            s[i] = 'q'           # 리스트 순회하며 문자 뒤집기
        elif s[i] == 'q' :
            s[i] = 'p'
        elif s[i] == 'b' :
            s[i] = 'd'
        elif s[i] == 'd' :
            s[i] = 'b'
 
    s = ''.join(s)               # 리스트를 문자열로 합치기
 
    print(f'#{case+1} {s[::-1]}')   # 슬라이싱으로 순서를 뒤집어서 출력
