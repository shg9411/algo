import sys
input = sys.stdin.readline


def main():
    def dfs(i):
        for want in cow[i]:
            if check[want]:
                continue
            check[want] = True
            if house[want] == 0 or dfs(house[want]):
                house[want] = i
                return True
        return False

    n, m = map(int, input().split())
    house = [0]*(m+1)
    res = 0
    cow = {i: list(map(int, input().split()))[1:] for i in range(1, n+1)}

    for i in range(1, n+1):
        check = [False]*(m+1)
        if dfs(i):
            res += 1
    print(res)


if __name__ == '__main__':
    main()
