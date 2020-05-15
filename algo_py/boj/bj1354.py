n, p, q, x, y = map(int, input().split())


def get(num):
    if num <= 0:
        return 1
    if num in val:
        return val[num]
    a = get(num//p-x)
    b = get(num//q-y)
    val[num] = a+b
    return val[num]


val = dict()
print(get(n))
