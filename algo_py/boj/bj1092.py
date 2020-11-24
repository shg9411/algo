n = int(input())
crane = sorted(map(int, input().split()), reverse=True)
m = int(input())
box = sorted(map(int, input().split()), reverse=True)
if box[0] > crane[0]:
    print(-1)
    exit()


def binary_search(s, e):
    def check(v):
        if n*v < m:
            return False
        for i in range(v, m, v):
            if box[i] > crane[i//v]:
                return False
        return True
    while s <= e:
        mid = (s+e) >> 1
        if check(mid):
            ans = mid
            e = mid-1
        else:
            s = mid+1
    return ans


print(binary_search(1, m))
