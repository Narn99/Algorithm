import sys

stk = []
N = int(sys.stdin.readline().rstrip())

for _ in range(N) :
    command = sys.stdin.readline().rstrip()
    if 'push' in command :
        a, b = command.split()
        stk.append(b)
    elif 'pop' in command :
        if not stk :
            print(-1)
        else :
            print(stk.pop())
    elif 'top' in command :
        if not stk :
            print(-1)
        else :
            print(stk[-1])
    elif 'size' in command :
        print(len(stk))
    else :
        if not stk :
            print(1)
        else :
            print(0)