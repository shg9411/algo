import sys
input = sys.stdin.readline


def main():

    def find(x):
        if x == p[x]:
            return x
        p[x] = find(p[x])
        return p[x]

    def union(x, y):
        x = find(x)
        y = find(y)
        if x < y:
            p[y] = x
        else:
            p[x] = y

    n = int(input())
    p = [i for i in range(n)]
    m = int(input())
    for i in range(n):
        tmp = list(map(int, input().split()))
        for j in range(n):
            if i != j and tmp[j] == 1:
                union(i, j)

    ans = set()
    for n in map(lambda x: int(x)-1, input().split()):
        ans.add(find(n))
        if len(ans) > 1:
            print("NO")
            exit()
    print("YES")


if __name__ == '__main__':
    main()
