# ccc = [5, 10, 92, 80, 77, 60, 777, 60, 520, 20, 31, 21, 9, 60]

import sys

def merge_sort(lst) :
    s = 0
    e = len(lst)

    def sort(s, e) :
        if e-s < 2 : return
        m = (s+e) // 2
        sort(s, m)
        sort(m, e)

        merge(s, m, e)

    def merge(s, m, e) :
        l = s
        h = m
        k = 0

        while l < m and h < e :
            if arr[l] <= arr[h] :
                tmp[k] = arr[l]
                l += 1
                k += 1
            else :
                tmp[k] = arr[h]
                h += 1
                k += 1

        while l < m :
            tmp[k] = arr[l]
            l += 1
            k += 1

        while h < e :
            tmp[k] = arr[h]
            h += 1
            k += 1

        for i in range(s, e) :
            arr[i] = tmp[i-s]

    return sort(s, e)


N = int(sys.stdin.readline())
arr = [int(sys.stdin.readline()) for _ in range(N)]
tmp = [0]*N
merge_sort(arr)

for i in range(N) :
    print(arr[i])