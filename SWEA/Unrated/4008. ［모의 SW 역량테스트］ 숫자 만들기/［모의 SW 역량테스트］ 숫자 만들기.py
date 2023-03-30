# 숫자 만들기
# 경우의 수 만들고, 백트래킹.. 최대 최소 둘 다 구해야하는데 가지치기가 되나?

def dfs(n, op, result) :
    global mx, mn
    if n == N :
        if result > mx :        # 최댓값과 최솟값 갱신
            mx = result
        if result < mn :
            mn = result
        return
    else :
        a = nlst[n]
        if op[0] > 0 :   # 각 연산자가 남아있으면 빼면서 연산 해주고, 연산자 리스트 다시 복구
            op[0] -= 1
            dfs(n+1, op, result + a)
            op[0] += 1

        if op[1] > 0 :
            op[1] -= 1
            dfs(n+1, op, result - a)
            op[1] += 1

        if op[2] > 0 :
            op[2] -= 1
            dfs(n+1, op, result * a)
            op[2] += 1

        if op[3] > 0 :
            op[3] -= 1
            dfs(n+1, op, int(result / a))  # 소수점 아래는 버리기..
            op[3] += 1

T = int(input())

for case in range(1, T+1) :

    N = int(input())
    op_lst = list(map(int, input().split()))
    nlst = list(map(int, input().split()))
    mx = -1e9
    mn = 1e9

    dfs(1, op_lst, nlst[0])

    print(f'#{case} {mx-mn}')