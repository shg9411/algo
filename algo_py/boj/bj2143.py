def main():
    t = int(input())
    n = int(input())
    a = list(map(int, input().split()))
    m = int(input())
    b = list(map(int, input().split()))
    aDict = dict()
    for i in range(n):
        val = 0
        for j in range(i, n):
            val += a[j]
            aDict[val] = aDict.get(val,0)+1

    res = 0
    for i in range(m):
        val = 0
        for j in range(i, m):
            val += b[j]
            if t-val in aDict:
                res += aDict[t-val]

    print(res)


if __name__ == '__main__':
    main()