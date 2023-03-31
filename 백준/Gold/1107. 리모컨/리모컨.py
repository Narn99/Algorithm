# 리모컨
# 대강 N을 분해하고.. 해당 자리수의 수가 고장났는지 안 났는지 확인.
# 안 났다면 그 수를 입력하고, 고장났다면 그 다음 자리수를 확인해서 +1을 하는지 -1을 하는지 선택.
# 650번을 가야하는데, 6이 고장이라면? 599 -> 600 -> 650...
# 500000을 가려면 511111 --> 11117번
# 즉 입력 못 하는 숫자가 나오면, 거기서부터 입력 가능한 숫자 중 가장 가까운 수로 만든 뒤에,
# 거기서부터는 전부 +나 -로 다가가야하는 것. => 두 수 차이의 절댓값
# 근데 98, 99, 101, 102같은 경우엔 +나 - 누르는게 더 빠르다.

import sys

def check(n, lst) :
    global ans

    if n <= ln+1:
        if lst :
            cnt = abs(int(N) - int(''.join(map(str, lst)))) + len(lst)
            if cnt < ans :
                ans = cnt
        for i in button :
            check(n+1, lst + [i])
    return

N = sys.stdin.readline().rstrip()
Nlst = list(map(int,list(N)))
M = int(sys.stdin.readline())
ln = len(N)
button = []

if M > 0 :
    broken = list(map(int, sys.stdin.readline().split()))
else :
    broken = []

for btn in range(10) :
    if btn not in broken :
        button.append(btn)

ans = abs(int(N) - 100)

check(0, [])

print(ans)