numlst = []
maxnum = 0                      # 숫자들을 넣어줄 리스트, 그리고 최댓값과 최댓값이 몇 번째 있을지 넣어줄 정수 설정
maxnumth = 0

for num in range(9) :
    nownum = int(input())       # for문으로 순회하며 정수를 입력받고, 그 정수를 numlst 리스트에 넣어준다.
    numlst += [nownum]
    if nownum > maxnum :        # 만약 현재의 입력받은 숫자가 현 최댓값보다 크다면, 최댓값을 바꿔주고 현재가 몇 번째인지 기록해준다.
        maxnum = nownum
        maxnumth = num+1

print(maxnum)
print(maxnumth)