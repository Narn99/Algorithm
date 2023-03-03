# 암호 생성기
# 감소량을 1씩 늘려가며 감소 후 맨 뒤로 이동. (맨 뒤로 이동은 그냥 원형 큐로 인덱스 순회하면 됨)
# 순회하며 1씩 늘어나는 감소량만큼 감소시키고, 그게 0보다 작아지는 때 값은 0으로 하며 종료하기.
# 그 0보다 작아지는 인덱스는 마지막 자리로 이동한 상태까지가 최종 암호.
 
while True :
    try :
        tc = int(input())
        numlst = list(map(int,input().split()))
        idx = 0
        ans = []
 
        while True :
            numlst[idx%8] -= 1 + (idx%5)    # 순회해가며 1~5를 빼줌
            if numlst[idx%8] <= 0 :
                numlst[idx%8] = 0           # 값이 0 이하가 될 때, 그 값을 마지막으로 하기 위해 idx에 +1
                idx += 1
                break
            idx += 1
 
        for i in range(8) :
            ans += [numlst[(idx+i)%8]]      # 0이 된 값부터 나열한걸 ans에 넣어줌
 
        ans = ' '.join(map(str,ans))
 
        print(f'#{tc} {ans}')
 
    except :
        break