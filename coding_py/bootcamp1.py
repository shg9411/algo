arr = [1, 2, 3, 3, 3, 4, 4]
arrr = [3, 2, 4, 4, 2, 5, 2, 5, 5]
arrrr = [3, 5, 7, 9, 1]


def solve(x):
    tmp = set()
    ret = []
    for val in x:
        if val not in tmp:
            ret.append(x.count(val)) if x.count(val) > 1 else None
        tmp.add(val)
    return ret if ret else [-1]


print(solve(arrr))
