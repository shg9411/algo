def solve():
    def m_sort(arr):
        if len(arr) <= 1:
            return arr
        mid = len(arr) // 2
        l = arr[:mid]
        r = arr[mid:]
        l = m_sort(l)
        r = m_sort(r)
        return merge(l, r)

    def merge(l, r):
        res = []
        while len(l) > 0 or len(r) > 0:
            if len(l) > 0 and len(r) > 0:
                if cmp(l[0], r[0]):
                    res.append(l[0])
                    l = l[1:]
                else:
                    res.append(r[0])
                    r = r[1:]
            elif len(l) > 0:
                res.append(l[0])
                l = l[1:]
            elif len(r) > 0:
                res.append(r[0])
                r = r[1:]
        return res

    def cmp(i, j):
        if pos[i] != pos[j]:
            return pos[i] < pos[j]
        i += d
        j += d
        if i < l and j < l:
            return pos[i] < pos[j]
        else:
            return i > j

    def quick_sort(arr):
        if len(arr) <= 1:
            return arr
        pivot = arr[len(arr) // 2]
        pos_pivot = pos[pivot]
        lt, eq, gt = [], [], []
        for num in arr:
            if pos[num] < pos_pivot:
                lt.append(num)
            elif pos[num] > pos_pivot:
                gt.append(num)
            else:
                if num+d < l and pivot+d < l:
                    if pos[num+d] < pos[pivot+d]:
                        lt.append(num)
                    elif pos[num+d] > pos[pivot+d]:
                        gt.append(num)
                    else:
                        eq.append(num)
                elif num+d > pivot+d:
                    lt.append(num)
                elif pivot+d > num+d:
                    gt.append(num)
                else:
                    eq.append(num)
        return quick_sort(lt) + eq + quick_sort(gt)

    s = input()
    l = len(s)
    lcp = [0]*l
    arr = [-1]*l
    pos = [-1]*l
    for i in range(l):
        arr[i] = i
        pos[i] = s[i]
    d = 1
    while 1:
        arr = quick_sort(arr)
        tmp = [0] * l
        for i in range(l-1):
            tmp[i+1] = tmp[i] + cmp(arr[i], arr[i+1])
        for i in range(l):
            pos[arr[i]] = tmp[i]
        if tmp[-1] == l-1:
            break
        d *= 2
    k = 0
    for i in range(l):
        k = max(k-1, 0)
        if pos[i] == l-1:
            continue
        j = arr[pos[i]+1]
        while i+k < l and j+k < l and s[i+k] == s[j+k]:
            k += 1
        lcp[pos[i]] = k
    print(max(lcp[:-1]))


if __name__ == '__main__':
    solve()
