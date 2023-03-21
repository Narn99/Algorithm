import sys
from collections import deque

T = int(sys.stdin.readline())

for case in range(1, T+1) :

    p = sys.stdin.readline().rstrip()
    n = int(sys.stdin.readline())
    lst = sys.stdin.readline().rstrip().lstrip('[').rstrip(']').split(',')
    n_lst = deque()
    for num in lst :
        try :
            n_lst.append(int(num))
        except :
            pass

    f = 0
    b = len(n_lst)
    ans = ''
    Rcnt = 0

    for word in p :
        if word == 'R' :
            Rcnt = (Rcnt+1)%2
        else :
            if Rcnt == 1 :
                b -= 1
            else :
                f += 1
            if f > b:       # f가 b를 지나치면 종료
                print('error')
                break
    else :
        ans = list(lst)[f:b]
        if Rcnt == 1 :
            ans.reverse()
        print('['+','.join(ans)+']')


