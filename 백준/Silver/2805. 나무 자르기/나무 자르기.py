# 나무 자르기
# 최소 M 이상은 챙기기 위해 설정할 높이의 최댓값
# 나무 높이 내림차순으로 정렬해서, 나무개수 카운팅하며 그 다음 나무 높이까지 자르고.
# 만약 그게 M보다 크다면 멈추고, 그 나무 포함 안 하고 높이 높이기.

import sys

def check() :

    cnt = 1
    sm = 0

    for i in range(1, N+1):
        height = trees[i]
        sm += (trees[i - 1] - height) * cnt # 이전 나무 높이에서 현재 나무 높이를 뺀 값 * 그 이전까지 나무 개수
        if sm == M:
            print(height)
            return
        elif sm > M:    # 현재 가져갈 나무가 M보다 더 많다면 줄여야함.
            s = height
            e = trees[i-1]
            while True :       # 두 나무 사이에서 높이를 이진 탐색으로 찾기
                m = (s+e)//2
                if s <= e :
                    if sm - (m-height)*cnt == M :
                        print(m)
                        return
                    elif sm - (m-height)*cnt > M :
                        s = m+1
                    else :
                        e = m-1
                else :
                    print(e)   # 하다가 s가 e보다 커지면, 정수 안에는 딱 맞는 값이 없는거니
                    return     # e가 sm > M이 되게 하는 높이의 최댓값이다
        cnt += 1

N, M = map(int, sys.stdin.readline().split())
trees = list(map(int, sys.stdin.readline().split()))+[0]  # 마지막에 높이가 0인 것까지 확인하기 위해 0 추가
trees.sort(reverse=True)

check()