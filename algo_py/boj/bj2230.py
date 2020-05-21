import sys
input = sys.stdin.readline


def main():
    N, M = map(int, input().split())
    num = [int(input()) for _ in range(N)]
    num.sort()
    i = j = 0
    res = sys.maxsize
    while i < N and j < N:
        diff = num[j]-num[i]
        if M < diff:
            i += 1
            if diff < res:
                res = diff
        elif M > diff:
            j += 1
        else:
            res = M
            break
    print(res)


if __name__ == '__main__':
    main()