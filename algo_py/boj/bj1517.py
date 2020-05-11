n = int(input())
num = list(map(int, input().split()))
cnt = 0


def merge(l, m, r):
    global cnt
    i = j = 0
    len_1 = m-l
    len_2 = r-m
    tmp = []
    while i < len_1 and j < len_2:
        if num[l+i] > num[m+j]:
            cnt += len_1-i
            tmp.append(num[m+j])
            j += 1
        else:
            tmp.append(num[l+i])
            i += 1
    while i < len_1:
        tmp.append(num[l+i])
        i += 1
    while j < len_2:
        tmp.append(num[m+j])
        j += 1
    for idx in range(l, r):
        num[idx] = tmp[idx-l]


def mergesort(l, r):
    global cnt
    if r == l+1:
        return
    if r == l+2:
        if num[l] > num[l+1]:
            cnt += 1
            num[l], num[l+1] = num[l+1], num[l]
        return
    m = (l+r)//2
    mergesort(l, m)
    mergesort(m, r)
    merge(l, m, r)


mergesort(0, n)
print(cnt)
