def kth(a: list, k: int):
    k = k-1
    s = 0
    e = len(a)-1
    while 1:
        i, j = s, e
        while 1:
            while i <= e and a[i] <= a[s]:
                i += 1
            while a[j] > a[s]:
                j -= 1
            if i >= j:
                break
            a[i], a[j] = a[j], a[i]
        a[s], a[j] = a[j], a[s]
        if j == k:
            return a[j]
        elif j < k:
            s = j+1
        else:
            e = j-1