import sys
input = sys.stdin.readline

if __name__ == '__main__':
    n = int(input())
    q = list(map(int, input().split()))
    for _ in range(n-1):
        q += list(map(int, input().split()))
        q = sorted(q, reverse=True)[:n]
    print(q[n-1])
