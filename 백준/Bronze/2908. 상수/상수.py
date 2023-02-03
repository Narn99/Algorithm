N = list(input().split())

a = list(N[0])
b = list(N[1])

a = int(''.join(a[::-1]))
b = int(''.join(b[::-1]))           # 리스트 슬라이싱으로 뒤집기

if a > b :
    print(a)
else :
    print(b)