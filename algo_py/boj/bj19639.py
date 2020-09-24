import sys
input = sys.stdin.readline


def solve():
    x, y, m = map(int, input().split())
    lose = []
    potion = []
    for _ in range(x):
        lose.append(int(input()))
    for _ in range(y):
        potion.append(int(input()))

    if m+sum(potion) <= sum(lose):
        print(0)
        exit()

    i = j = 0
    hp = m//2
    cur = m
    while i < x and j < y:
        if cur > hp:
            print(-i-1)
            cur -= lose[i]
            i += 1
        else:
            print(j+1)
            cur += potion[j]
            j += 1

    while i < x:
        print(-i-1)
        i += 1
    while j < y:
        print(j+1)
        j += 1


if __name__ == "__main__":
    solve()
