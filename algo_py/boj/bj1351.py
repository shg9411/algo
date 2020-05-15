n, p, q = map(int, input().split())


def get(num):
    if num in val:
        return val[num]
    x = get(num//p)
    y = get(num//q)
    val[num] = x+y
    return val[num]


val = dict()
val[0] = 1
print(get(n))
