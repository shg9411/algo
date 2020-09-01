import sys
input = sys.stdin.readline


def main():
    def find(x):
        if x == parent[x]:
            return x
        parent[x] = find(parent[x])
        return parent[x]

    def union(x, y):
        x = find(x)
        y = find(y)
        if A[x] <= A[y]:
            parent[y] = x
        else:
            parent[x] = y
    N, M, k = map(int, input().split())
    parent = [i for i in range(N+1)]
    A = [0]+list(map(int, input().split()))
    for _ in range(M):
        v, w = map(int, input().split())
        union(v, w)
    friends = set()
    res = 0
    print(parent)
    for i in range(1, N+1):
        idx = find(i)
        if idx not in friends:
            friends.add(idx)
            res += A[idx]
    print(res if res <= k else "Oh no")


if __name__ == '__main__':
    main()
