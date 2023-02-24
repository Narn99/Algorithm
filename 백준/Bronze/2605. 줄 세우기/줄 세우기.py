# 줄 세우기
# 줄을 서는데, 자기 포함한 끝 인덱스에서 뽑은 번호만큼 뺀 위치로 가기.

N = int(input())
nums = list(map(int,input().split()))
lst = []

for i in range(len(nums)) :
    if not lst :
        lst.append(i+1)
    else :
        idx = len(lst)
        lst.insert(idx-nums[i], i+1)    # 해당 인덱스에 넣어주기

print(' '.join(map(str,lst)))