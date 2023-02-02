def d(n) :

    ni = list(map(int,list(str(n))))
    result = 0

    for i in ni :
        result += i

    return n + result

# n은 d(n)의 생성자

lst = []

for i in range(1, 10001) :              # 1부터 10000까지 있는 리스트 작성
    lst += [i]

a = 1

while a < 10000 :                   # a값이 1만 될 때까지 
    if d(a) in lst :
        lst.remove(d(a))            # d(a)가 lst 안에 있다면 제거
    a += 1

for num in lst :
    print(num)
