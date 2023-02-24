# 나무 조각 ~ 버블정렬

nums = list(map(int, input().split()))

for i in range(len(nums)) :
    for j in range(len(nums)-1) :       # 앞에서부터 버블 정렬하며 매번 출력
        if nums[j] > nums[j+1] :
            nums[j], nums[j+1] = nums[j+1], nums[j]
            print(' '.join(map(str,nums)))