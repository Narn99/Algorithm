# 비밀 이메일
# N글자를 적는다. R*C=N인 수에서 R<=C일 때, R이 가장 큰 값을 선택.
# 행이 R개, 열이 C개인 행렬을 만들어서 1행부터 마지막 행까지 순서대로 채운다.
# 그리고 그걸 첫번째 열부터 꺼내서 받아 읽는다.

word = input()
N = len(word)
n = int(N**0.5)     # R = C인 상황이 제곱해서 N이 되는 때고, 그 때가 최대니까 0.5제곱까지만 구함.
mx_n = 0

for i in range(1, n+1) :
    if N % i == 0 and i > mx_n :    # 1부터 n까지 중, N을 나누어 떨어트리는 수 중 최댓값을 고름
        mx_n = i

R, C = mx_n, N//mx_n
arr = [['']*C for _ in range(R)]
cnt = 0
ans = ''

for j in range(C) :
    for i in range(R) :
        arr[i][j] = word[cnt]   # 열부터 채워주고
        cnt += 1

for i in range(R) :
    for j in range(C) :         # 행부터 뽑아줌
        ans += arr[i][j]

print(ans)