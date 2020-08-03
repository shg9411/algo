import sys
input = sys.stdin.readline


def find(a):
    if parent[a] == a:
        return a
    parent[a] = find(parent[a])
    return parent[a]


def union(a, b):
    a = find(a)
    b = find(b)
    parent[a] = b


if __name__ == '__main__':
    g = int(input())
    p = int(input())
    parent = [i for i in range(g+1)]
    res = 0
    for _ in range(p):
        tmp = int(input())
        dock = find(tmp)
        if not dock:
            break
        union(dock, dock-1)
        res += 1
    print(res)
