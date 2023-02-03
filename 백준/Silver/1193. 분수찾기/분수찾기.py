# [1/1] [1/2 2/1] [3/1 2/2 1/3] [1/4 2/3 3/2 4/1] [5/1 4/2 3/3 2/4 1/5] ...

X = int(input())

i = 0
check = 0

while True :
    if check >= X :
        break
    i += 1
    check += i

mn = check - X

if i % 2 == 0 :
    print(f'{i - mn}/{1 + mn}')
else :
    print(f'{1+mn}/{i-mn}')