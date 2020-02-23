import sys
sys.setrecursionlimit(10**6)


def solve(a, k):
    a.insert(0, 0)
    pivot = a[(len(a)+1)//2 - 1]
    left, mid, right = [], [], []
    for i in range(len(a)):
        if a[i] < pivot:
            left.append(a[i])
        elif a[i] > pivot:
            right.append(a[i])
        else:
            mid.append(a[i])

    if k < len(left):
        return solve(left, k)
    elif k < len(left) + len(mid):
        return mid[0]
    else:
        return solve(right, k - len(left) - len(mid))


a = [5, 4, 3]
k = 3
print(solve(a, k))
